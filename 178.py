user_input = input("Введите слово: ")
s = user_input.replace(" ", "").lower()

is_palindrome = True
length = len(s)

for i in range(length // 2):
    if s[i] != s[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Это слово палиндром!")
else:
    print("Это слово не палиндром.")
