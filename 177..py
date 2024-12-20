def roman_to_decimal(roman):
    roman_numerals = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    if not roman:
        return 0
     first_value = roman_numerals[roman[0]]
    if len(roman) > 1:
        second_value = roman_numerals[roman[1]]
        if first_value < second_value:
            return roman_to_decimal(roman[1:]) - first_value
        else:
            return first_value + roman_to_decimal(roman[1:])
    else:
        return first_value
def main():
    user_input = input("Введите число в римских цифрах: ")
    decimal_value = roman_to_decimal(user_input)
    print(f"Десятичное представление числа {user_input}: {decimal_value}")
if __name__ == "__main__":
    main()
