def wave_type(frequency):
    frequency = float(frequency)
    ranges = {
        (0, 3e9): "Радиоволны",
        (3e9, 3e12): "Микроволны",
        (3e12, 4.3e14): "Инфракрасное излучение",
        (4.3e14, 7.5e14): "Видимое излучение",
        (7.5e14, 3e17): "Ультрафиолетовое излучение",
        (3e17, 3e19): "Рентгеновское излучение",
        (3e19, float('inf')): "Гамма-излучение" # float('inf') - бесконечность
    }
    for (min_freq, max_freq), wave in ranges.items():
        if min_freq <= frequency < max_freq:
            return wave
    return "Некорректное значение частоты"

while True:
    try:
        freq_str = input("Частота (Гц) или 'quit': ")
        if freq_str.lower() == 'quit':
            break
        freq = float(freq_str)
        print(f"Тип волны: {wave_type(freq)}")
    except ValueError:
        print("Неверный ввод")
