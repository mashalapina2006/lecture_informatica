note_frequencies = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88
}
user_frequency = float(input("Введите частоту звука в Гц: "))
note_found = False
for note, frequency in note_frequencies.items():
    if abs(user_frequency - frequency) <= 1:
        print("Соответствующая нота: ", note)
        note_found = True
        break
if not note_found:
    print("Ноты, соответствующей введенной частоте, не существует.")
