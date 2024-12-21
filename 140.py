province_map = {
    'A': 'Новая Шотландия',
    'B': 'Нью-Брансуик',
    'C': 'Принца Эдварда',
    'E': 'Квебек',
    'G': 'Квебек',
    'H': 'Квебек',
    'J': 'Квебек',
    'K': 'Онтарио',
    'L': 'Онтарио',
    'M': 'Онтарио',
    'N': 'Онтарио',
    'P': 'Онтарио',
    'R': 'Манитоба',
    'S': 'Саскачеван',
    'T': 'Альберта',
    'V': 'Британская Колумбия',
    'Y': 'Юкон',
    'X': 'Северо-Западные территории или Нунавут'
}

def check_postal_code(postal_code):
    if len(postal_code) != 6:
        return "Ошибка: почтовый индекс должен состоять из 6 символов."
    
    first_char = postal_code[0].upper()
    second_char = postal_code[1]

    if first_char not in province_map:
        return "Ошибка: первый символ не используется в почтовых индексах Канады."
    
    if not second_char.isdigit():
        return "Ошибка: второй символ должен быть цифрой."

    province = province_map[first_char]
    area_type = "сельская" if second_char == '0' else "городская"
    
    return f"Провинция: {province}, Тип территории: {area_type}."

if __name__ == "__main__":
    user_input = input("Введите почтовый индекс: ")
    result = check_postal_code(user_input)
    print(result)
