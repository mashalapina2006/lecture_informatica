import random
def generate_password(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line.strip().capitalize() for line in file if len(line.strip()) >= 3]
        if len(words) < 2:
            print("Недостаточно слов в файле для генерации пароля.")
            return
        password = random.choice(words) + random.choice(words)
        if 8 <= len(password) <= 10:
            print(f"Сгенерированный пароль: {password}")
        else:
            print("Пароль не соответствует требованиям по длине.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
if __name__ == "__main__":
    file_path = input("Введите имя файла со списком слов: ")
    generate_password(file_path)
