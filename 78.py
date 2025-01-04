def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2  
        else:
            n = n * 3 + 1  
    sequence.append(1)  
    return sequence

while True:
    user_input = int(input("Введите положительное целое число (или 0/отрицательное для выхода): "))
    if user_input <= 0:
        print("Выход из программы.")
        break
    result = collatz_sequence(user_input)
    print("Сиракузская последовательность:", result)



