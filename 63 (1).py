n = float(input("Введите число: "))
if n == 0:
    print("Ошибка: первым числом не может быть 0")
else:
    numbers = list()
    while n != 0:
        numbers.append(n)
        n = float(input("Введите число: "))
    print(f"Среднее значение: {sum(numbers) / len(numbers)}")

