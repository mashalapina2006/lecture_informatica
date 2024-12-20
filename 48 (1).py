def get_zodiac_sign(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif month == 1 and day >= 20 or month == 2 and day <= 18:
        return "Водолей"
    elif month == 2 and day >= 19 or month == 3 and day <= 20:
        return "Рыбы"
    elif month == 3 and day >= 21 or month == 4 and day <= 19:
        return "Овен"
    elif month == 4 and day >= 20 or month == 5 and day <= 20:
        return "Телец"
    elif month == 5 and day >= 21 or month == 6 and day <= 20:
        return "Близнецы"
    elif month == 6 and day >= 21 or month == 7 and day <= 22:
        return "Рак"
    elif month == 7 and day >= 23 or month == 8 and day <= 22:
        return "Лев"
    elif month == 8 and day >= 23 or month == 9 and day <= 22:
        return "Дева"
    elif month == 9 and day >= 23 or month == 10 and day <= 22:
        return "Весы"
    elif month == 10 and day >= 23 or month == 11 and day <= 21:
        return "Скорпион"
    elif month == 11 and day >= 22 or month == 12 and day <= 21:
        return "Стрелец"
    else:
        return "Ошибка: неверная дата"

while True:
    try:
        day = int(input("Введите день рождения: "))
        month = int(input("Введите месяц рождения (число от 1 до 12): "))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            print("Неверная дата")
            continue
        sign = get_zodiac_sign(day, month)
        print(f"Ваш знак зодиака: {sign}")
        break
    except ValueError:
        print("Неверный формат ввода. Пожалуйста, введите числа.")
