import random
import os 

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For MacOS and Linux (os.name is 'posix')
    else:
        os.system('clear')


def print_chord(chord):
    if vertical == True:
        print_vertical_chord(chord)
        return 
    for chord_string in chord:
        for chord_tret in chord_string:
            print(chord_tret, end=" ")
        print("\n")

def print_vertical_chord(chord):
    transposed = [list(col)[::-1] for col in zip(*chord)]
    for chord_tret in transposed:
        for chord_string in chord_tret:
            symbol = chord_string.replace("-", "|")
            print(symbol, end=" ")
        print("\n")



def init_base_chord(chord_to_init):
    chord_to_init = [["-" for _ in range(6)] for _ in range(6)]
    for item in chord_to_init:
        item[0] = "X"
    return chord_to_init

def init_open_A_chord(chord_to_init):
    #Line,Column

    #Playble strings
    chord_to_init[0][0] = "O"
    chord_to_init[1][0] = "O"
    chord_to_init[2][0] = "O"
    chord_to_init[3][0] = "O"
    chord_to_init[4][0] = "O"

    #Notes
    chord_to_init[1][2] = "3"
    chord_to_init[2][2] = "1"
    chord_to_init[3][2] = "2"

def init_open_A_minor_chord(chord_to_init):
    #Line,Column

    #Playble strings
    chord_to_init[0][0] = "O"
    chord_to_init[1][0] = "O"
    chord_to_init[2][0] = "O"
    chord_to_init[3][0] = "O"
    chord_to_init[4][0] = "O"

    #Notes
    chord_to_init[1][1] = "1"
    chord_to_init[2][2] = "3"
    chord_to_init[3][2] = "2"

def init_open_D_chord(chord_to_init):
    #Line,Column

    #Playble strings
    chord_to_init[0][0] = "O"
    chord_to_init[1][0] = "O"
    chord_to_init[2][0] = "O"
    chord_to_init[3][0] = "O"

    #Notes
    chord_to_init[1][2] = "2"
    chord_to_init[3][2] = "1"
    chord_to_init[2][3] = "3"

def init_open_D_minor_chord(chord_to_init):
    #Line,Column

    #Playble strings
    chord_to_init[0][0] = "O"
    chord_to_init[1][0] = "O"
    chord_to_init[2][0] = "O"
    chord_to_init[3][0] = "O"

    #Notes
    chord_to_init[0][1] = "1"
    chord_to_init[1][3] = "4"
    chord_to_init[2][2] = "2"

def init_open_E_chord(chord_to_init):
    #Line,Column

    #Playble strings
    chord_to_init[0][0] = "O"
    chord_to_init[1][0] = "O"
    chord_to_init[2][0] = "O"
    chord_to_init[3][0] = "O"
    chord_to_init[4][0] = "O"
    chord_to_init[5][0] = "O"

    #Notes
    chord_to_init[2][1] = "1"
    chord_to_init[3][2] = "3"
    chord_to_init[4][2] = "2"

def init_open_E_minor_chord(chord_to_init):
    #Line,Column

    #Playble strings
    chord_to_init[0][0] = "O"
    chord_to_init[1][0] = "O"
    chord_to_init[2][0] = "O"
    chord_to_init[3][0] = "O"
    chord_to_init[4][0] = "O"
    chord_to_init[5][0] = "O"

    #Notes
    chord_to_init[3][2] = "3"
    chord_to_init[4][2] = "2"

def print_all_chords():
    print("\n A chord") 
    print_chord(a_chord)
    print("\n D chord") 
    print_chord(d_chord)
    print("\n E chord") 
    print_chord(e_chord)
    print("\n Am chord") 
    print_chord(a_minor_chord)
    print("\n Em chord") 
    print_chord(e_minor_chord)
    print("\n Dm chord") 
    print_chord(d_minor_chord)

def quiz():
    chords_to_quiz = [{'chord_name':'a','chord':a_chord},
                      {'chord_name':'am','chord':a_minor_chord},
                      {'chord_name':'e','chord':e_chord},
                      {'chord_name':'em','chord':e_minor_chord},
                      {'chord_name':'d','chord':d_chord},
                        {'chord_name':'dm','chord':d_minor_chord},]

    while True:
        randon_chord_index = random.randint(0, 4)  # Between 0 and 4 (inclusive)

        print("What chord is this ? (type exit to Exit)")
        print_chord(chords_to_quiz[randon_chord_index]['chord'])
        chord_option = input(">")
        if chord_option.lower() == "exit":
            break
        if chord_option.lower() == chords_to_quiz[randon_chord_index]['chord_name']:
            print("\n\033[92m Yeah! your're a master! \033[0m") #green$
        else:
            print (f"\n\033[91m Nop... the answer was {chords_to_quiz[randon_chord_index]['chord_name']} \033[0m")
        input("press enter to continue")



a_chord,a_minor_chord,d_chord,d_minor_chord,e_chord,e_minor_chord = [],[],[],[],[],[]

a_chord = init_base_chord(a_chord)
init_open_A_chord(a_chord)

a_minor_chord = init_base_chord(a_minor_chord)
init_open_A_minor_chord(a_minor_chord)

d_chord = init_base_chord(d_chord)
init_open_D_chord(d_chord)

d_minor_chord = init_base_chord(d_minor_chord)
init_open_D_minor_chord(d_minor_chord)

e_chord = init_base_chord(e_chord)
init_open_E_chord(e_chord)

e_minor_chord = init_base_chord(e_minor_chord)
init_open_E_minor_chord(e_minor_chord)

vertical = True

while True:
    clear_console()
    print(f"Chord display mode \033[33m {'vertical' if vertical else 'horizontal'}\033[0m\n\n\n")
    print("Options:\n\tC: Print a Chord \n\tA: Print all Chords \n\tQ: Chord Quiz \n\tT: Toogle Vertical\n\tE: Exit")
    main_option = input(">")
    if main_option.lower()=="a":
        print_all_chords()
    elif main_option.lower()=="e":
        break
    elif main_option.lower()=="t":
        vertical = not vertical
        continue
    elif main_option.lower()=="q":
        quiz()
        continue
    elif main_option.lower()=="c":
        chord_option = input("What chord to Print? >")
        if chord_option.lower() == "a":
            print_chord(a_chord)
        elif chord_option.lower() == "am":
            print_chord(a_minor_chord)
        elif chord_option.lower() == "d":
            print_chord(d_chord)
        elif chord_option.lower() == "dm":
            print_chord(d_minor_chord)
        elif chord_option.lower() == "e":
            print_chord(e_chord)
        elif chord_option.lower() == "em":
            print_chord(e_minor_chord)
        else:
            print("We dont have that chord!")
            break
    input("press enter to continue")
    



