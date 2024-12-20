def скорость_падения(высота):
    g = 9.8  
    начальная_скорость = 0 
    конечная_скорость = (начальная_скорость ** 2 + 2 * g * высота) ** 0.5
    return round(конечная_скорость, 1)
высота = float(input("Введите высоту в метрах: "))
скорость = скорость_падения(высота)
print(f"Скорость при соприкосновении с землей: {скорость} м/с")
