import os
import random
import mido
from mido import MidiFile, MidiTrack, Message

def generate_scale(root, scale_type):
    """
    Generate a musical scale based on the given root note and scale type.

    Parameters:
    - root (str): The root note of the scale (e.g., "C", "E", "F#").
    - scale_type (str): The type of scale to generate (e.g., "major", "minor", "phrygian", etc.).

    Returns:
    - list: A list of notes in the generated scale.
    """
    # All possible notes in one octave
    all_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    # Intervals (in semitones) for different scale types
    scales = {
        "major": [2, 2, 1, 2, 2, 2, 1],          # Major scale
        "minor": [2, 1, 2, 2, 1, 2, 2],          # Natural minor scale
        "phrygian": [1, 2, 2, 2, 1, 2, 2],       # Phrygian mode
        "aeolian": [2, 1, 2, 2, 1, 2, 2],        # Aeolian mode (same as natural minor)
        "chromatic": [1] * 12,                   # Chromatic scale (all semitones)
        "dorian": [2, 1, 2, 2, 2, 1, 2],         # Dorian mode
        "harmonic_minor": [2, 1, 2, 2, 1, 3, 1]  # Harmonic minor scale
    }

    # Get the intervals for the chosen scale
    intervals = scales[scale_type]
    root_index = all_notes.index(root)  # Find the index of the root note in the list
    scale = [root]  # Start the scale with the root note

    # Build the scale by adding intervals
    for interval in intervals:
        root_index = (root_index + interval) % len(all_notes)  # Wrap around the octave
        scale.append(all_notes[root_index])
    
    # Return generated scale
    return scale

def generate_random_rhythm(num_of_notes):
    """
    Generates a random rhythm sequence consisting of notes and rests.

    Parameters:
    - num_of_notes (int): The number of notes and rests to generate in the rhythm sequence.

    Returns:
    - list: A list containing a sequence of notes and rests (as strings).
    """
    # Define possible note and rest lengths
    note_lengths = ["1", "1/2", "1/4", "1/8", "1/16", "1/8 dotted", "1/16 dotted", "1/2 dotted", "1 dotted"]
    rest_lengths = ["1", "1/2", "1/4", "1/8", "1/16", "1/8 dotted", "1/16 dotted", "1/2 dotted", "1 dotted"]

    # Initialize an empty list to store the generated rhythm
    rhythm = []

    # Loop to generate a sequence of notes and rests
    for _ in range(num_of_notes):
        # Randomly decide whether this beat is a note or a rest
        # True = note, False = rest
        note_or_rest = random.choice([True, False])
        if note_or_rest:
            rhythm.append(random.choice(note_lengths))  # Add a random note length
        else:
            rhythm.append(("rest", random.choice(rest_lengths)))  # Add a random rest length

    # Return the generated rhythm sequence
    return rhythm

def validate_num_of_notes(value):
    """
    Validate that the input is a positive integer.
    """
    if not value.isdigit() or int(value) <= 0:
        raise ValueError("Number of notes must be a positive integer.")
    return int(value)

def validate_root_note(value):
    """
    Validate that the input is a valid root note.
    """
    valid_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    value = value.upper()
    if value not in valid_notes:
        raise ValueError(f"Invalid root note: '{value}'. Valid notes are: {valid_notes}")
    return value

def validate_scale_type(value):
    """
    Validate that the input is a supported scale type.
    """
    valid_scales = ['major', 'minor', 'phrygian', 'aeolian', 'chromatic', 'dorian', 'harmonic_minor']
    value = value.lower()
    if value not in valid_scales:
        raise ValueError(f"Invalid scale type: '{value}'. Valid types: {valid_scales}")
    return value

def validate_octave(value):
    """
    Validate that the input is an integer between 1 and 8 (inclusive).
    """
    if not value.isdigit() or not (1 <= int(value) <= 8):
        raise ValueError("Octave must be an integer between 1 and 8.")
    return int(value)
    
def generate_riff(num_of_notes, root, scale_type, octave):
    """
    Generates a random riff by combining a musical scale with a random rhythm.

    Parameters:
    - num_of_notes (int): The number of notes to generate in the riff.
    - root (str): The root note of the scale.
    - scale_type (str): The type of scale to generate.
    - octave (int): The octave to append to each note.

    Returns:
    - list: A list of lists containing [note/rest, rhythm].
    """
    # Generate the scale and rhythm
    scale = generate_scale(root, scale_type)
    rhythm = generate_random_rhythm(num_of_notes)

    # Generate riff by randomly selecting notes or rests
    riff = []
    for r in rhythm:
        if "rest" in r:  # If it's a rest, keep it unchanged
            riff.append([r[0], r[1]])# Keep the rest and its duration in a list
        else:  # Otherwise, pick a random note from the scale and add the octave
            random_note = random.choice(scale) + str(octave)
            riff.append([random_note, r]) # Append the note and its duration in a list

    return riff

def save_riff_to_midi(riff, output_filename="djentify_riff.mid", ticks_per_beat=480):
    """
    Saves the generated riff to a MIDI file.

    Parameters:
    - riff (list): A list of lists containing [note/rest, rhythm].
    - output_filename (str): The name of the output MIDI file.
    - ticks_per_beat (int): The number of ticks per beat in the MIDI file.
    """
    # Get the absolute path to the current script directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the export folder path inside the same folder as the script
    export_dir = os.path.join(base_dir, "MIDI Exports")
    os.makedirs(export_dir, exist_ok=True)  # Ensure export folder exists

    # Combine export path with filename
    output_filename = os.path.join(export_dir, output_filename)

    # Create a new MIDI file and track
    midi = MidiFile(ticks_per_beat=ticks_per_beat)
    track = MidiTrack()
    midi.tracks.append(track)

    # Set tempo
    tempo = mido.bpm2tempo(120)
    track.append(mido.MetaMessage('set_tempo', tempo=tempo))

    # Add notes and rests to the MIDI track
    for item in riff:
        note = item[0]
        rhythm = item[1]

        duration_ticks = duration_to_ticks(rhythm, ticks_per_beat)  # Convert rhythm to MIDI duration

        if note == "rest":
            track.append(mido.Message('note_off', time=duration_ticks))  # Add a pause by delaying the next event
        else:
            midi_note = note_to_midi(note)
            track.append(mido.Message('note_on', note=midi_note, velocity=64, time=0))
            track.append(mido.Message('note_off', note=midi_note, velocity=64, time=duration_ticks))

    # Save the MIDI file to the specified path
    midi.save(output_filename)

def note_to_midi(note):
    """
    Converts a note name (e.g., "C4", "A4", "C#4") to its corresponding MIDI number.
    """
    note_map = {
        "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11
    }
    
    # Check if the note is a double-character note (e.g., "C#", "D#")
    if note[1] == '#':
        note_name = note[:2]
        octave = int(note[2:])
    else:
        note_name = note[0]
        octave = int(note[1:])

    # Convert to MIDI number using the note_map and octave shift
    midi_number = note_map[note_name] + (octave + 1) * 12  # Octave shifting
    return midi_number

def duration_to_ticks(duration, ticks_per_beat=480):
    """
    Converts note/rest duration (e.g., "1", "1/2") to MIDI ticks (default 480 ticks per beat).
    """
    duration_mapping = {
        "1": 1.0,  # Whole note
        "1/2": 0.5,  # Half note
        "1/4": 0.25,  # Quarter note
        "1/8": 0.125,  # Eighth note
        "1/16": 0.0625,  # Sixteenth note
        "1/8 dotted": 0.1875,  # Dotted eighth note
        "1/16 dotted": 0.09375,  # Dotted sixteenth note
        "1/2 dotted": 0.75,  # Dotted half note
        "1 dotted": 1.5  # Dotted whole note
    }
    return int(duration_mapping.get(duration, 0.25) * ticks_per_beat)  # Default 1/4 note

def main():
    # Display the program's title
    print("🎸 Djent Riff Generator -- DJENTIFY 🎸")

    # Ask for the number of riff elements (notes/rests) to generate
    while True:
        try:
            num_of_notes = validate_num_of_notes(input("Enter number of riff elements to generate (each will be a note or a rest): "))
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Oops! {e}")  # Show error message if input is invalid

    # Ask for the root note (e.g., C, D#, A)
    while True:
        try:
            root = validate_root_note(input("Enter root note (e.g., C, D#, A): "))
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Oops! {e}")  # Show error message if input is invalid

    # Ask for the scale type (e.g., major, minor, phrygian)
    while True:
        try:
            scale_type = validate_scale_type(input("Enter scale type (options: major, minor, phrygian, aeolian, chromatic, dorian, harmonic_minor): "))
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Oops! {e}")  # Show error message if input is invalid

    # Ask for the desired octave (e.g., 2, 3, 4)
    while True:
        try:
            octave = validate_octave(input("Enter desired octave (e.g., 2, 3, 4): "))
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Oops! {e}")  # Show error message if input is invalid

    # Generate the riff using the user-provided parameters
    riff = generate_riff(num_of_notes, root, scale_type, octave)

    # Display the generated riff
    print("\nGenerated Riff:")
    for note, duration in riff:
        print(f"{note} - {duration}")

    # Ask if the user wants to save the riff as a MIDI file
    save = input("\nDo you want to save the riff as a MIDI file? (y/n): ").lower()
    if save == 'y':
        # Ask for the filename to save the MIDI file
        filename = input("Enter filename (default: djentify_riff.mid): ").strip()
        if not filename:
            filename = "djentify_riff.mid"  # Default filename if none provided
        elif not filename.lower().endswith(".mid"):
            filename += ".mid"  # Add .mid extension if not present
        save_riff_to_midi(riff, filename)  # Save the riff to a MIDI file
        print(f"✅ Riff saved to MIDI Exports/{filename}")
    else:
        print("MIDI file not saved.")  # Inform the user if the file is not saved

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()