line = input("Введите строку: ")
is_palindrome = True
i = 0
while i < len(line) / 2 and is_palindrome: 
    if line[i] != line[len(line) - i - 1]:
        is_palindrome = False
i = i + 1
if is_palindrome:
    print(line, " – это палиндром") 
else:
        print(line, " – это не палиндром")
