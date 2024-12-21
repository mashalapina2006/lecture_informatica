def hex2int(hex_char):
    hex_char = hex_char.upper()
    if hex_char in '0123456789ABCDEF':
        return int(hex_char, 16)
    else:
        raise ValueError("Ошибка")
def int2hex(decimal_number):
    if 0 <= decimal_number <= 15:
        return hex(decimal_number).upper()[2:]
    else:
        raise ValueError("Ошибка: Число должно быть в диапазоне от 0 до 15")
if __name__ == "__main__":
    try:
        hex_value = 'A'
        decimal_value = hex2int(hex_value)
        print(f"{hex_value} в десятичной системе: {decimal_value}")
        decimal_number = 10 
        hex_value_converted = int2hex(decimal_number)
        print(f"{decimal_number} в шестнадцатеричной системе: {hex_value_converted}")
    except ValueError as e:
        print(e)