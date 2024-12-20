from math import sqrt
perimeter = 0
first_x = float(input("Введите первую координату X: ")) 
first_y = float(input("Введите первую координату Y: "))
x = first_x 
prev_y = first_y
line = input("Введите следующую координату X (Enter для окончания ввода): ") 
while line != "": 
    x = float(line) 
y = float(input("Введите следующую координату Y: "))
dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2) 
perimeter = perimeter + dist
prev_x = x 
prev_y = y
line = input("Введите следующую координату X (Enter для окончания ввода): ")
dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
perimeter = perimeter + dist
print("Периметр многоугольника равен", perimeter)

