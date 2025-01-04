import string
def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
user_input = input("Введите строку для проверки на палиндром: ")
if is_palindrome(user_input):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")

