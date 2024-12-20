letter = input("Введите букву латинского алфавита: ").lower()
if letter in 'aeiou':
    print("Эта буква гласная.")
elif letter == 'y':
    print("Эта буква может быть как гласной, так и согласной.")
else:
    print("Эта буква согласная.")
