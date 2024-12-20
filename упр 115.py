def find_proper_divisors(number):
    return [i for i in range(1, number) if number % i == 0]

if __name__ == "__main__":
    try:
        if (num := int(input("Введите целое число: "))) > 0:
          print("Собственные делители числа", num, ":", find_proper_divisors(num))
        else:
          print("Пожалуйста, введите положительное целое число.")
    except ValueError:
        print("Некорректный ввод.")
