import numpy as np
import sounddevice as sd
import fluidsynth

def note_name_to_number(note_name):
    """
    Convert a note name (in the format "A3", "Bb4", etc.) to a MIDI note number.

    :param note_name: The note name to convert.
    :return: The corresponding MIDI note number.
    """
    notes = {
        "C": 0,
        "C#": 1,
        "Db": 1,
        "D": 2,
        "D#": 3,
        "Eb": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "Gb": 6,
        "G": 7,
        "G#": 8,
        "Ab": 8,
        "A": 9,
        "A#": 10,
        "Bb": 10,
        "B": 11
    }

    note_number = notes[note_name[:-1]] + (int(note_name[-1]) + 1) * 12

    return note_number

def load_synth():
    # Load the soundfont file
    fs = fluidsynth.Synth()
    sfid = fs.sfload("FluidR3_GM.sf2")

    # Connect the synthesizer to the default audio output
    fs.start(driver="dsound")

    # Set the amplitude of the instrument
    fs.program_select(0, sfid, 0, 0)

    return fs

def play_notes(notes, duration=1, amplitude=0.5):
    """
    Play back a sample from a soundfont file at given note numbers, duration, and amplitude.

    :param notes: The MIDI note number(s) or note name(s) of the sample(s) to play.
    :param duration: The duration of the sample in seconds.
    :param amplitude: The amplitude of the sample (default=0.5).
    :param soundfont_path: The path to the soundfont file to use (default=None, which uses the default soundfont).
    :param sample_rate: The sample rate of the sample (default=44100).
    """


    # Convert note names to note numbers
    if isinstance(notes, str):
        notes = [notes]
    note_numbers = []
    for note in notes:
        if isinstance(note, str):
            note_number = note_name_to_number(note)
        else:
            note_number = note
        note_numbers.append(note_number)

    # Start playing the notes
    for note_number in note_numbers:
        fs.noteon(0, note_number, int(amplitude * 127))

    # Wait for the duration of the notes
    sd.sleep(int(duration * 1000))

    # Stop playing the notes
    for note_number in note_numbers:
        fs.noteoff(0, note_number)


fs = load_synth()

"""
play_notes(["D3"])
play_notes(["A3"])
play_notes(["D3","A3"])
"""