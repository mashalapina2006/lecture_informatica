line = input("Введите 8 бит информации:")
while line != "": 
    if line.count("0") + line.count("1") != 8 or len(line) != 8: 
        print("Это не 8 бит… Попробуйте еще.")
    else: ones = line.count("1")
    if ones % 2 == 0:
        print("Бит честности должен иметь значение 0")
else: print("Бит четности должен иметь значение 1.")
line = input("Введите 8 бит информации: ")