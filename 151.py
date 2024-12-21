import sys
if len(sys.argv) < 2:
    print("Ошибка: не заданы файлы для открытия.")
    sys.exit(1)
for filename in sys.argv[1:]:
    try:
        with open(filename) as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
