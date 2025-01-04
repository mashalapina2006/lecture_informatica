binary_input = input("Введите двоичное число: ")
decimal_value = 0
for index, bit in enumerate(reversed(binary_input)):
    decimal_value += int(bit) * (2 ** index)
print(f"Десятичное значение числа {binary_input} равно {decimal_value}.")




