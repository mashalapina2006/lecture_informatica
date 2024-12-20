feet = int(input("Введите количество футов: "))
inches = int(input("Введите количество дюймов: "))
total_inches = (feet * 12) + inches
centimeters = total_inches * 2.54
print(f"Ваш рост в сантиметрах: {centimeters:.2f}")
