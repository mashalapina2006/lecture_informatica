def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a 
if __name__ == "__main__":
    a = float(input("Введите длину первой стороны"))
    b = float(input("Введите длину второй стороны"))
    c = float(input("Введите длину третьей стороны"))
    if triangle(a, b, c):
        print("Треугольник может быть построен")
    else:
        print("Треугольник не может быть построен")
