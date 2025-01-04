def prime_factors(n):
    factors = []
    factor = 2  

    while factor <= n:
        if n % factor == 0:  
            factors.append(factor)  
            n //= factor  
        else:
            factor += 1  

    return factors
user_input = int(input("Введите целое число (больше или равно 2): "))

if user_input < 2:
    print("Ошибка: число должно быть больше или равно 2.")
else:
    result = prime_factors(user_input)
    print("Простые множители числа:", result)



