import random
max_value = random.randint(1, 100)
change_count = 0
print(max_value)
for _ in range(99):
    current_value = random.randint(1, 100)
    print(current_value) 
    if current_value > max_value:
        max_value = current_value
        change_count += 1
        print("Обновлен максимум!")
print(f"\nМаксимальное число: {max_value}")
print(f"Количество смен максимального значения: {change_count}")






