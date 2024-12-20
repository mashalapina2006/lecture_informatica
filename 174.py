while True:
    try:
        a = int(input("Первое число (или 'q' для выхода): "))
        if str(a).lower() == 'q':
            break
        b = int(input("Второе число: "))
        while b:
            a, b = b, a % b
        print(f"НОД: {a}")
    except ValueError:
        print("Ошибка: введите целые числа.")
