negatives, zeros, positives = [], [], []

while (num_str := input("Введите целое число или Enter: ")):
    try:
        num = int(num_str)
        (negatives if num < 0 else zeros if num == 0 else positives).append(num)
    except ValueError:
        print("Некорректный ввод. Введите целое число.")

print(*negatives, sep='\n')
print(*zeros, sep='\n')
print(*positives, sep='\n')
