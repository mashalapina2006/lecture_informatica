import sys
if len(sys.argv) < 2:
    print("Ошибка: не задан аргумент командной строки (имя файла).")
    sys.exit(1)
filename = sys.argv[1]
try:
    with open(filename) as file:
        lines = file.readlines()[-10:]
        print(''.join(lines))
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не найден.")
