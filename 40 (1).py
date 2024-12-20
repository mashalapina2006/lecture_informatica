def noise_level_description(db):
    noise_levels = {
        0: "Тишина",
        10: "Шепот",
        30: "Обычный разговор",
        60: "Шумный офис",
        80: "Громкий концерт",
        100: "Двигатель самолета на взлете"
    }
    
    min_db = min(noise_levels.keys())
    max_db = max(noise_levels.keys())

    if db < min_db:
        return f"Уровень шума ниже минимального ({min_db} дБ)."
    elif db > max_db:
        return f"Уровень шума выше максимального ({max_db} дБ)."
    elif db in noise_levels:
        return f"{db} дБ соответствует: {noise_levels[db]}."
    else:
        lower = max([key for key in noise_levels.keys() if key < db], default=None)
        upper = min([key for key in noise_levels.keys() if key > db], default=None)
        
        if lower is not None and upper is not None:
            return f"Уровень шума {db} дБ находится между {lower} дБ ({noise_levels[lower]}) и {upper} дБ ({noise_levels[upper]})."
        else:
            return "Не удалось определить уровни шума."

try:
    user_input = float(input("Введите уровень шума в децибелах: "))
    result = noise_level_description(user_input)
    print(result)
except ValueError:
    print("Ошибка: введите корректное число.")
