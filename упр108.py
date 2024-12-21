def convert_volume(teaspoons):
    cups = teaspoons // 48
    tablespoons = (teaspoons % 48) // 3
    remaining_teaspoons = teaspoons % 3
    result = []
    if cups > 0:
        result.append(f"{cups} cup{'s' * (cups > 1)}")
    if tablespoons > 0:
        result.append(f"{tablespoons} tablespoon{'s' * (tablespoons > 1)}")
    if remaining_teaspoons > 0:
        result.append(f"{remaining_teaspoons} teaspoon{'s' * (remaining_teaspoons > 1)}")
        return ', '.join(result)
def main():
    try:
        teaspoons = int(input("Введите количество чайных ложек"))
        if teaspoons < 0:
            print("Ошибка")
        else:
            result = convert_volume(teaspoons)
            print(f"Объем: {result}")
    except ValueError:
        print("Ошибка")
if __name__ == "__main__":
    main()
