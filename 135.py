def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if numbers[p]:
            for i in range(p*p, limit + 1, p):
                numbers[i] = False
    return [i for i, is_prime in enumerate(numbers) if is_prime]

if __name__ == "__main__":
    try:
        limit = int(input("Введите верхнюю границу: "))
        if limit < 0:
            print("Граница должна быть неотрицательной.")
        else:
            primes = sieve_of_eratosthenes(limit)
            print(f"Простые числа от 2 до {limit}: {primes}")
    except ValueError:
        print("Некорректный ввод. Введите целое число.")
