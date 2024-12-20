def get_color(wavelength):
    if 380 <= wavelength < 450:
        return "Фиолетовый"
    elif 450 <= wavelength < 495:
        return "Синий"
    elif 495 <= wavelength < 570:
        return "Зеленый"
    elif 570 <= wavelength < 590:
        return "Желтый"
    elif 590 <= wavelength < 620:
        return "Оранжевый"
    elif 620 <= wavelength <= 750:
        return "Красный"
    return "Длина волны вне видимого спектра"
try:
    wavelength = float(input("Введите длину волны в нанометрах (нм): "))
    print(get_color(wavelength))
except 
    print("Ошибка: введите числовое значение.")
