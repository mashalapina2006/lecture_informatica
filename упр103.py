import random
import string
def is_password_strong(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    attempts = 0
    password = ''
    while not is_password_strong(password):
        password = generate_random_password()
        attempts += 1
    print(f"Сгенерированный надежный пароль: {password}")
    print(f"Количество попыток: {attempts}")
