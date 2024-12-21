def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def nextPrime(n):
    next_number = n + 1
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1
if __name__ == "__main__":
    user_input = input("Введите целое число: ")
    try:
        number = int(user_input)
        next_prime = nextPrime(number)
        print(f"Первое простое число, большее {number}: {next_prime}")
    except ValueError:
        print("Ошибка")
