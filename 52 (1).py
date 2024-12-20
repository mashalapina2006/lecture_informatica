def earthquake_level(magnitude):
    levels = [(2.0, "Минимальное"), (3.0, "Очень слабое"), (4.0, "Слабое"), (5.0, "Промежуточное"), (6.0, "Умеренное"), (7.0, "Сильное"), (8.0, "Очень сильное"), (10.0, "Огромное"), (float('inf'), "Разрушительное")]
    for mag, level in levels:
        if magnitude < mag:
            return level
    return "Ошибка"

while True:
    try:
        mag = float(input("Магнитуда (или 0 для выхода): "))
        if mag == 0:
            break
        print(f"Уровень: {earthquake_level(mag)}")
    except ValueError:
        print("Неверный ввод")
