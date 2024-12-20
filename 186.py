data = input("Введите строку для сжатия: ")

if not data:
    encoded = []
else:
    encoded = []
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append((count, data[i - 1]))
            count = 1

    encoded.append((count, data[-1]))

print("Закодированный список:", encoded)
