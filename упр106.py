def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def days_in_month(month, year):
    if month < 1 or month > 12:
        return
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
def main():
     try:
        month = int(input("Введите номер месяца"))
        year = int(input("Введите год"))
        days = days_in_month(month, year)
        print(f"Количество дней в месяце {month} года {year}: {days}")
     except ValueError:
        print("Ошибка")
if __name__ == "__main__":
    main()
