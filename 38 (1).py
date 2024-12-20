def determine_shape(sides):
    if sides < 3 or sides > 10:
        return "Ошибка: количество сторон должно быть от 3 до 10."
    shapes = {
        3: "Треугольник",
        4: "Квадрат",
        5: "Пятиугольник",
        6: "Шестигранник",
        7: "Семигранник",
        8: "Восьмигранник",
        9: "Девятигранник",
        10: "Десятигранник"
    }
    return shapes[sides]

try:
    sides = int(input("Введите количество сторон фигуры (от 3 до 10): "))
    shape_name = determine_shape(sides)
    print(shape_name)
except ValueError:
    print("Ошибка: введите целое число.")
