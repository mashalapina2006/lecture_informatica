def to_decimal(num_str, base):
    return int(num_str, base)
def from_decimal(num, base):
    if num == 0:
        return '0'
    digits = ''
    while num > 0:
        remainder = num % base
        if remainder > 9:
            digits += chr(remainder + 55)
        else:
            digits += str(remainder)
        num //= base
    return digits[::-1]
def main():
    try:
        source_base = int(input("Введите исходную систему счисления (от 2 до 16)"))
        target_base = int(input("Введите целевую систему счисления (от 2 до 16)"))
        if not (2 <= source_base <= 16) or not (2 <= target_base <= 16):
            print("Ошибка")
            return
        number = input(f"Введите число в системе счисления {source_base}: ")
        decimal_number = to_decimal(number, source_base)
        converted_number = from_decimal(decimal_number, target_base)
        print(f"Число {number} в системе {source_base} преобразовано в {converted_number} в системе {target_base}.")
    except ValueError:
        print("Ошибка.")
if __name__ == "__main__":
    main()
