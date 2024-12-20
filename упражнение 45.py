holidays = {
    (1, 1): "Новый год",
    (7, 1): "День Канады",
    (12, 25): "Рождество"
}
day = int(input("Введите день (число от 1 до 31): "))
month = int(input("Введите месяц (число от 1 до 12): "))
holiday_name = holidays.get((month, day))
if holiday_name:
    print(f"{holiday_name} отмечается {day} {month}.")
else:
    print(f"На {day} {month} праздники не приходятся.")
