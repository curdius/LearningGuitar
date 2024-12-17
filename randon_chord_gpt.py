import random
import os
import time
import sys
import argparse
import pyttsx3
import datetime

# Default known chords
known_chords = ["A", "Am", "C", "D", "Dm", "E", "Em", "G"]

def load_input_parameters():
    # Define arguments
    parser = argparse.ArgumentParser(description="Practice random chord changes!")
    
    parser.add_argument(
        '--chords', '-c',
        nargs='+',
        help='List of Chords',
        required=False,
        default=known_chords)
    parser.add_argument("--type", default="speed", type=str, help="Type of Game")
    parser.add_argument("--rep", default=20, type=int, help="Repetitions at each step")
    parser.add_argument("--step", default=0.25, type=float, help="Increasing time at each step")
    parser.add_argument("--startspeed", default=3, type=float, help="Speed at start")
    parser.add_argument("--min", default=0.5, type=float, help="Minimal Step: Max speed")
    parser.add_argument("--speed", default=2, type=float, help="Constant Speed: On Stable Game")
    parser.add_argument("--duration", default=300, type=float, help="Game Duration: On Stable Game")
    
    args = parser.parse_args()
    return args

def clear_console():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        print("\n" * 100)  # Fallback

def log_chord(chord):
    with open("chord_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {chord}\n")

def play_speed_game(a_rep, a_start_speed, a_step, a_min, chords):
    NUMBER_OF_CHANGES_PER_EACH_TIME = a_rep
    starting_time_interval = a_start_speed
    time_interval_count = NUMBER_OF_CHANGES_PER_EACH_TIME

    clear_console()
    print("Welcome to the Random Speed Chord Game!")
    print(f"Starting at {a_start_speed} secs, {a_rep} repetitions per step, decreasing by {a_step} secs until {a_min} secs.")
    input("Press Enter to start!")

    print(f"@ {starting_time_interval} secs")
    while starting_time_interval > a_min:
        chord_to_play = random.choice(chords)
        if time_interval_count == 0:
            starting_time_interval -= a_step
            time_interval_count = NUMBER_OF_CHANGES_PER_EACH_TIME
            print(f"@ {starting_time_interval:.2f} secs")

        print(f"\a\n\n\nPLAY:\t\033[1m{chord_to_play}\033[0m")
        engine.say(chord_to_play)
        engine.runAndWait()
        log_chord(chord_to_play)

        time_interval_count -= 1
        time.sleep(starting_time_interval)

    print("Game Over! Great job!")

def play_static_game(a_speed, a_duration, chords):
    clear_console()
    print(f"Welcome to the Static Chord Game! Play at {a_speed} secs for {a_duration} secs.")
    input("Press Enter to start!")
   
    start_time = time.time()

    while time.time() - start_time < a_duration:
        chord_to_play = random.choice(chords)
        print(f"\a\n\n\nPLAY:\t\033[1m{chord_to_play}\033[0m")
        engine.say(chord_to_play)
        engine.runAndWait()
        log_chord(chord_to_play)

        time.sleep(a_speed)

    print("Time's up! Great practice session!")

# Initialize
args = load_input_parameters()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

# Start game
if args.type.strip().lower() == "speed":
    play_speed_game(args.rep, args.startspeed, args.step, args.min, args.chords)
elif args.type.strip().lower() == "static":
    play_static_game(args.speed, args.duration, args.chords)
else:
    print("Invalid game type! Choose 'speed' or 'static'.")
