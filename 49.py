chinese_zodiac = {
    0: "Обезьяна",
    1: "Петух",
    2: "Собака",
    3: "Свинья",
    4: "Крыса",
    5: "Бык",
    6: "Тигр",
    7: "Кролик",
    8: "Дракон",
    9: "Змея",
    10: "Лошадь",
    11: "Коза"
}
year = int(input("Введите ваш год рождения: "))
zodiac_animal = chinese_zodiac[year % 12]
print("Ваше животное по китайскому гороскопу: ", zodiac_animal)

