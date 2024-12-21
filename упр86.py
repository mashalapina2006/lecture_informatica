start_fare = 4.00  
rate_per_140m = 0.25  
def calculate_taxi_fare(distance_km):
    distance_m = distance_km * 1000
    section = distance_m // 140
    total_fare = start_fare + (section * rate_per_140m)
    return total_fare
print("Введите расстояние поездки в километрах.")
distance = float(input("Расстояние (км): "))
fare = calculate_taxi_fare(distance)
print("Стоимость поездки составляет: $", fare)
