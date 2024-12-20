C = 4.186 
cost_per_kWh = 0.089  
m = float(input("Введите массу воды в граммах (или миллилитрах): "))
delta_T = float(input("Введите требуемую разницу температур (ΔT) в °C: "))
q = m * C * delta_T
q_kWh = q / 3600000  
cost = q_kWh * cost_per_kWh
print(f"Необходимое количество энергии (q): {q:.2f} Дж")
print(f"Стоимость нагрева: ${cost:.2f}")
