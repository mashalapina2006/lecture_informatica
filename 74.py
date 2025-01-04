def newton_sqrt(x):
    guess = x / 2.0
    tolerance = 1e-12
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2.0
    return guess
try:
    x = float(input("Введите число для вычисления квадратного корня: "))
    if x < 0:
        print("Квадратный корень из отрицательного числа не определен.")
    else:
        sqrt_x = newton_sqrt(x)
        print(f"Квадратный корень из {x} приближенно равен {sqrt_x}")
except ValueError:
    print("Пожалуйста, введите корректное число.")

