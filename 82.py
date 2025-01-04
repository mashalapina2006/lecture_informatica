decimal_input = int(input("Введите целое число: "))
result = ""
q = decimal_input
while q != 0:
    r = q % 2
    result = str(r) + result
    q //= 2
print(f"Двоичное представление числа {decimal_input} равно {result}.")





