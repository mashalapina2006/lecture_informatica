def remove_outliers(data, n):
    return sorted(data)[n:-n] if len(data) >= 2 * n + 1 else None

if __name__ == "__main__":
    numbers = []
    while (num := input("Введите целое число или 'готово': ")).lower() != 'готово':
        try:
            numbers.append(int(num))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число или 'готово'.")

    if len(numbers) < 4:
        print("Ошибка: нужно минимум 4 числа.")
    else:
        modified_list = remove_outliers(numbers, 1)
        if modified_list:
            print("Оригинальный список:", numbers)
            print("Измененный список:", modified_list)
        else:
           print("Ошибка: Слишком мало чисел для удаления экстремальных значений.")
