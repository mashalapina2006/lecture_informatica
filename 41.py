a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))
if a == b == c:
    triangle_type = "равносторонний"
elif a == b or b == c or a == c:
    triangle_type = "равнобедренный"
else:
    triangle_type = "разносторонний"
print(f"Треугольник является {triangle_type}.")
