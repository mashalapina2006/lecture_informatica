month = input("Введите название месяца: ").lower()
day = int(input("Введите номер дня: "))
if (month == 'декабрь' and day >= 21) or (month == 'январь') or (month == 'февраль') or (month == 'март' and day < 20):
    season = "Зима"
elif (month == 'март' and day >= 20) or (month == 'апрель') or (month == 'май') or (month == 'июнь' and day < 21):
    season = "Весна"
elif (month == 'июнь' and day >= 21) or (month == 'июль') or (month == 'август') or (month == 'сентябрь' and day < 22):
    season = "Лето"
elif (month == 'сентябрь' and day >= 22) or (month == 'октябрь') or (month == 'ноябрь') or (month == 'декабрь' and day < 21):
    season = "Осень"
else:
    season = "Некорректная дата"
print("Сезон: ", season)
