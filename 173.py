def sum_recursive():
    user_input = input("Введите число (или нажмите Enter для завершения): ")
    if user_input == "":
        return 0.0
    try:
        number = float(user_input)
        return number + sum_recursive()
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        return sum_recursive()
total_sum = sum_recursive()
print(f"Сумма значений: {total_sum}")
