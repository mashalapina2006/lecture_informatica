def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    user_input = input("Введите целое число: ")
    try: 
        number = int(user_input)
        result = is_prime(number)
        if result:
            print(f"{number} является простым числом.")
        else:
            print(f"{number} не является простым числом.")
    except ValueError:
        print("Ошибка")
