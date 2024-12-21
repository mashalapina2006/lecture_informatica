def calculate_median(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]
print("Введите три числа")
num1 = float(input("Первое число"))
num2 = float(input("Второе число"))
num3 = float(input("Третье число"))
median = calculate_median(num1, num2, num3)
print("Медиана введенных чисел", median)
