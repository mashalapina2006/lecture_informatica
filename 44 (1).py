banknotes = {
    1: "Джордж Вашингтон",
    2: "Томас Джефферсон",
    5: "Авраам Линкольн",
    10: "Александр Гамильтон",
    20: "Эндрю Джексон",
    50: "Улисс Грант",
    100: "Бенджамин Франклин"
}

while True:
    try:
        denomination = int(input("Введите номинал банкноты (или 0 для выхода): "))
        if denomination == 0:
            break
        if denomination in banknotes:
            print(f"На банкноте номиналом ${denomination} изображен {banknotes[denomination]}.")
        else:
            print("Банкноты с таким номиналом не существует.")
    except ValueError:
        print("Неверный формат ввода. Пожалуйста, введите число.")
