notes_c4 = {
    "C": 261.63,
    "C#": 277.18,
    "D": 293.66,
    "D#": 311.13,
    "E": 329.63,
    "F": 349.23,
    "F#": 369.99,
    "G": 392.00,
    "G#": 415.30,
    "A": 440.00,
    "A#": 466.16,
    "B": 493.88
}

def get_note_frequency(note_str):
    try:
        note, octave_str = note_str.upper().rstrip('#').split(sep = '')
        octave = int(octave_str)
        base_frequency = notes_c4[note]
        if note[-1] == '#':
          note = note[:-1] + '#'
        frequency = base_frequency * (2* (4 - octave))
        return frequency
    except (KeyError, ValueError):
        return "Неверный формат"

while True:
    note_input = input("Нота (или 'quit'): ")
    if note_input.lower() == 'quit':
        break
    frequency = get_note_frequency(note_input)
    print(f"Частота: {frequency}")
