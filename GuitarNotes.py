import random
import os 
from tabulate import tabulate
import matplotlib.pyplot as plt

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For MacOS and Linux (os.name is 'posix')
    else:
        os.system('clear')

# Chromatic scale with both English and solfège notation
chromatic_scale = [
    {"english": "C", "solfege": "Do"},
    {"english": "C#", "solfege": "Do#"},
    {"english": "D", "solfege": "Re"},
    {"english": "D#", "solfege": "Re#"},
    {"english": "E", "solfege": "Mi"},
    {"english": "F", "solfege": "Fa"},
    {"english": "F#", "solfege": "Fa#"},
    {"english": "G", "solfege": "Sol"},
    {"english": "G#", "solfege": "Sol#"},
    {"english": "A", "solfege": "La"},
    {"english": "A#", "solfege": "La#"},
    {"english": "B", "solfege": "Si"}
]

# Guitar strings with starting notes (English notation)
guitar_strings = [
    {"Number": "6", "Note": "E"},
    {"Number": "5", "Note": "A"},
    {"Number": "4", "Note": "D"},
    {"Number": "3", "Note": "G"},
    {"Number": "2", "Note": "B"},
    {"Number": "1", "Note": "E"}
]

# Function to get the note at a given fret
def get_note_at_fret(start_note, fret, system="english"):
    # Find the index of the starting note in the chromatic scale
    start_index = next(i for i, note in enumerate(chromatic_scale) if note["english"] == start_note)
    # Calculate the index for the target note
    note_index = (start_index + fret) % len(chromatic_scale)
    # Return the note in the specified system
    return chromatic_scale[note_index][system]

# Function to display all notes on the guitar
def display_guitar_notes(strings, num_frets, system="english"):
    for string in strings:
        # Get the string note in the specified system
        start_note_english = string["Note"]
        start_note = next(note[system] for note in chromatic_scale if note["english"] == start_note_english)
        
        string_number = string["Number"]
        print(f"String {string_number} ({start_note} in {system}):")
        
        for fret in range(num_frets + 1):  # Include 0 for the open string
            note = get_note_at_fret(start_note_english, fret, system)
            print(f"  Fret {fret}: {note}")
        print()

def print_guitar_notes_scheme(num_frets, system="english"):
    output_array = []
    
    for fret in range(num_frets + 1):  # Include 0 for the open string
        new_col = []
        for string in guitar_strings:
            start_note_english = string["Note"]
            start_note = next(note[system] for note in chromatic_scale if note["english"] == start_note_english)
        
            string_number = string["Number"]
            note = get_note_at_fret(start_note_english, fret, system)
            #print(note, end=" ")
            new_col.append(note)
        output_array.append(new_col)
        #print()

    #transposed = list(map(list, zip(*output_array)))
    print_fret_board(output_array)


def print_fret_board(toPrint):

    transposed = [list(col)[::] for col in zip(*toPrint)]

    print(tabulate(transposed, tablefmt="plain"))

    # Example fret marker positions: single markers at {3,5,7,9,15,17,19}, double marker at {12}.
    single_markers = {3,5,7,9,15,17,19}
    double_marker = 12

    strings = len(transposed[0])       # Number of strings
    frets = len(transposed)      # Number of frets per string

    #fig, ax = plt.subplots(figsize=(10, strings))
    #plt.subplots_adjust(bottom=0.2)  # Make space for the slider

    print (f"transposed:{transposed}")

    fig, ax = plt.subplots(figsize=(frets, strings * 0.5))

    # Define the width range for line thickness
    max_width = 3.0  # thickest line on the left (fret 0)
    min_width = 1.0  # thinnest line on the right (last fret)

    # Offset for lines to appear to the right of the text
    line_offset_for_notes = 0.2
    marker_horizontal_offset = -0.7  # Place fret markers to the left of the line
    marker_vertical_position = -1 / 2.0  # Center vertically among the strings



    # Draw vertical lines for frets
    for s in range(strings):
        # Calculate line width that decreases from left to right
        if strings > 1:
            line_width = max_width - s * (max_width - min_width) / (strings - 1)
        else:
            # If there's only one fret, just use max_width
            line_width = max_width
        if s == double_marker and s < strings:
            # Double marker
            ax.text(marker_vertical_position,s + marker_horizontal_offset, "●●", 
                        ha='right', va='center', fontsize=12)
        # If not double marker, check for single markers
        elif s in single_markers and s < strings: #
            # Single marker
            ax.text(marker_vertical_position,s + marker_horizontal_offset, "●", 
                        ha='right', va='center', fontsize=12)
        
        #reversed_f = (frets - 1) - f
       # Shift lines slightly to the right using line_offset
        ax.plot([s, s], [0, strings-1], color='black', linewidth=line_width) #



    # Place notes slightly to the right of each fret line
    for i_f,f in enumerate(transposed):
        for i_s,s in enumerate(f):
    #for s in range(strings):
    #    for f in range(frets):
            print(f"{s},{f}")
            note = s #transposed[s][f]
            if i_s == 0:
                # Top line of notes: place them to the left of the line, bold, and right-aligned
                ax.text(i_f + line_offset_for_notes, i_s-line_offset_for_notes, note, ha='left', va='center', fontsize=14, fontweight='bold')
            else:
                # Other lines remain as before
                ax.text(i_f + line_offset_for_notes, i_s-line_offset_for_notes, note, ha='left', va='center', fontsize=14)

    # Add very light horizontal lines
    for s in range(strings):
        ax.axhline(y=s, color='lightgray', linewidth=0.5, zorder=0) 

    # Invert y-axis so string 1 is at the top
    ax.invert_yaxis()

    # Add some margin to the x and y axes to prevent clipping of notes
    # For example, extend the x-limit to the right by 1 extra unit
    ax.set_xlim(-2, frets)  # You can adjust these values as needed
    ax.set_ylim(strings, -1)  # Inverted axis, so top is larger

    # Remove axes ticks for a cleaner look
    ax.set_xticks([])
    ax.set_yticks([])

    plt.gcf().set_size_inches(frets, strings * 0.5)

    plt.tight_layout()
   #plt.ioff()  # Turn off interactive mode

    plt.show()
    plt.close(fig)

def get_total_sharp_in_string(string_array):
    total_sharps = 0
    for fret in string_array:
        if "#" in fret:
                total_sharps += 1
    return total_sharps



def get_max_sharps_per_line(note_matrix):
    max_sharps_per_line = 0
    for line in note_matrix:
        column_sharps_count = 0
        for col in line:
            if "#" in col:
                line_sharps_count += 1
        if line_sharps_count > max_sharps_per_line:
            max_sharps_per_line = line_sharps_count
    return max_sharps_per_line


    # for string in reversed(guitar_strings):
    #     # Get the string note in the specified system
    #     start_note_english = string["Note"]
    #     start_note = next(note[system] for note in chromatic_scale if note["english"] == start_note_english)
        
    #     string_number = string["Number"]
    #     #print(f"String {string_number} ({start_note} in {system}):")
    #     #print(start_note,end=" ")
        
    #     for fret in range(num_frets + 1):  # Include 0 for the open string
    #         note = get_note_at_fret(start_note_english, fret, system)
    #         print(note, end=" ")
    #     print()

# Example usage: Display notes ford 12 frets in both English and Solfège

def run_quiz():
    while True:
        random_string_number = random.randint(0, 5)  # Between 1 and 6 (inclusive)
        random_tret_number = random.randint(1, 20)  # Between 1 and 20 (inclusive)
        
        print(f'\nWhat is the note on string {guitar_strings[random_string_number]["Note"]} and tret {random_tret_number}:')
        answer = input(">")

        correct_answer = get_note_at_fret(guitar_strings[random_string_number]["Note"],random_tret_number)
        if answer.lower() == correct_answer.lower():
            print("\n\033[92m Yeah! your're a master! \033[0m") #green$
        elif answer.lower() == "exit":
            break
        else:
            print (f"\n\033[91m Nop... the answer was {correct_answer} \033[0m")



while True:
    clear_console()
   # print("Options:\n G-> Guitar Map in English\n GS-> Guitar Map in Solfege \n Q-> Quiz \n E-> Exit")
    user_input = input("Options:\n\t G-> Guitar Map in English\n\t GS-> Guitar Map in Solfege \n\t H-> Print Guitar Notes\n\t Q-> Quiz\n\t E-> Exit\n >")
    
    if user_input.lower() == 'e':  # Check if the user wants to exit
        print("Exiting... Goodbye!")
        break  # Break the loop to exit
    
    if user_input.lower() == "g":
        print("English Notation:")
        display_guitar_notes(guitar_strings, 20, system="english")
        cont = input("press any key to continue...")

    if user_input.lower() == "gs":
        print("English Notation:")
        display_guitar_notes(guitar_strings, 20, system="solfege")
        cont = input("press any key to continue...")

    if user_input.lower()=="h":
        print_guitar_notes_scheme(int(input("How many frets (from the top):")))
        cont = input("press any key to continue...")

    if user_input.lower() == "q":
        run_quiz()
