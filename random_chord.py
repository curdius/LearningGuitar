import random
import os
import time
import sys
import argparse
import pyttsx3

known_chords = ["A","Am","C","D","Dm","E","Em","G"]


def load_input_parameters():
    # Define arguments
    parser = argparse.ArgumentParser(description="My parameters")
    
    parser.add_argument(
    '--chords', '-c',
    nargs='+',  # Use '+' or '*' to accept multiple arguments
    help='List of Chords', default = known_chords)
    parser.add_argument("--type", default="speed",type=str, help="Type of Game")
    parser.add_argument("--rep", default=20,type=int, help="Repetitions at each step")
    parser.add_argument("--step", default=0.25,type=float, help="Increasing time at each step")
    parser.add_argument("--startspeed", default=3,type=float, help="speed at start")
    parser.add_argument("--min", default=0.5,type=float, help="Minimal Step: Max speeed")
    parser.add_argument("--speed", default=2,type=float, help="Constant Speed: On Stable Game")
    parser.add_argument("--duration", default=300,type=float, help="Game Duration: On Stable Game")
 

    args = parser.parse_args()
    return args

def clear_console():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        print("\n" * 100)  # Fallback: Print empty lines to simulate clearing

def play_speed_game(a_rep,a_start_speed,a_step,a_min,chords):
    NUMBER_OF_CHANGES_PER_EACH_TIME = a_rep
    starting_time_interval = a_start_speed
    time_interval_count = NUMBER_OF_CHANGES_PER_EACH_TIME
    clear_console()
    print("Welcome to the random fucking fast chord changes ! \n You will have to play faster and faster")
    print(f"Starting at {a_start_speed} secs, play {a_rep} x and after it will be {a_step} secs faster until {a_min} secs")

    input("Press Enter to Start!")
    print(f"@ {starting_time_interval} secs")
    while True:
        chord_to_play = chords[random.randint(0, len(chords)-1)]  
        if time_interval_count == 0:
            starting_time_interval = starting_time_interval - a_step
            time_interval_count = NUMBER_OF_CHANGES_PER_EACH_TIME
            print(f"@ {starting_time_interval} secs")

        print(f"\a\n\n\nPLAY:\t\033[1m{chord_to_play}\033[0m")
        engine.say(chord_to_play)
        engine.runAndWait()

        if starting_time_interval < a_min:
            break

        time_interval_count-=1
        time.sleep(starting_time_interval)
 
def play_static_game(a_speed,a_duration,chords):

    clear_console()
    print(f"Welcome to the easy thing!\n Play @ {a_speed} secs for {a_duration} secs")
    input("Press Enter to Start!")
   
    start_time = time.time()

    while True:
        chord_to_play = chords[random.randint(0, len(chords)-1)]
        
        print(f"\a\n\n\nPLAY:\t\033[1m{chord_to_play}\033[0m")
        engine.say(chord_to_play)
        engine.runAndWait()

        if time.time() - start_time > a_duration:
            print("We are done, hope your fingers are not hurting too much!")
            break

        time.sleep(a_speed)
 
 

args = load_input_parameters()
engine = pyttsx3.init()


if args.type.strip().lower() == "speed":
    play_speed_game(args.rep,args.startspeed,args.step,args.min,args.chords)
if args.type.strip().lower()== "static":
    play_static_game(args.speed,args.duration,args.chords)

