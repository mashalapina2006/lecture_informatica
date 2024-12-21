def is_password_strong(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit
if __name__ == "__main__":
    user_password = input("Введите пароль для проверки надежности: ")
    if is_password_strong(user_password):
        print("Пароль надежный")
    else:
        print("Пароль ненадежный")
