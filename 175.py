def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)
def main():
    user_input = input("Введите неотрицательное целое число: ")
    try:
        number = int(user_input)
        if number < 0:
            print("Ошибка: Введите неотрицательное целое число.")
        else:
            binary_representation = decimal_to_binary(number)
            print(f"Двоичное представление числа {number}: {binary_representation}")
    except ValueError:
        print("Ошибка: Введите корректное целое число.")
if __name__ == "__main__":
    main()
