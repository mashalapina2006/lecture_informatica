def get_rating_description(rating):
    if rating == 0.0:
        return "Низкий уровень"
    elif rating == 0.4:
        return "Удовлетворительный уровень"
    elif rating >= 0.6:
        return "Высокий уровень"
    else:
        return "Некорректное значение рейтинга"

while True:
    try:
        rating = float(input("Введите рейтинг сотрудника (0.0, 0.4, 0.6 или выше): "))
        description = get_rating_description(rating)
        if description == "Некорректное значение рейтинга":
            print(description)
            continue
        bonus = rating * 2400.00
        print(f"Рейтинг: {rating}, Описание: {description}, Прибавка к зарплате: ${bonus:.2f}")
        break
    except ValueError:
        print("Неверный формат ввода. Пожалуйста, введите число.")

        
