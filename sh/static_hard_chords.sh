#!/bin/bash
echo "Running random_chord.py with the following command:"
echo "python3 random_chord.py --type=static --speed=2 --duration=600 --chords A D Dm C G"

echo -n "Duration: "
read duration

echo -n "Speed: "
read speed

python3 ../random_chord.py --type=static --speed="$speed" --duration="$duration" --chords A D Dm C G
