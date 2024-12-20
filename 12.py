import math
t1 = float(input("Введите широту первой точки (градусы): "))
g1 = float(input("Введите долготу первой точки (градусы): "))
t2 = float(input("Введите широту второй точки (градусы): "))
g2 = float(input("Введите долготу второй точки (градусы): "))
t1_rad = math.radians(t1)
g1_rad = math.radians(g1)
t2_rad = math.radians(t2)
g2_rad = math.radians(g2)
distance = 6371.01 * math.acos(math.sin(t1_rad) * math.sin(t2_rad) + 
                                 math.cos(t1_rad) * math.cos(t2_rad) * 
                                 math.cos(g1_rad - g2_rad))
print(f"Расстояние между точками: {distance:.2f} км")
