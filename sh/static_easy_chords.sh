#!/bin/bash

echo -n "Duration: "
read duration

echo -n "Speed: "
read speed

echo "Running random_chord.py with the following command:"
echo "python3 ../random_chord.py --type=static --speed="$speed" --duration="$duration" --chords Am E Em"

python3 ../random_chord.py --type=static --speed="$speed" --duration="$duration" --chords Am E Em
