a = float(input()) 
b = float(input()) 
c = float(input()) 
discriminant = b * b - 4 * a * c 
if discriminant == 0: 
    print("У квадратичной функции 1 корень") 
    x = -b / (2 * a) 
    print(x) 
elif discriminant > 0: 
    print("У квадратичной функции 2 корня") 
    x = (-b + discriminant**0.5) / (2 * a) 
    print(x) 
    x = (-b - discriminant**0.5) / (2 * a) 
    print(x) 
else: 
    print("У квадратичной функции нет корней")
