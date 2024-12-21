import sys
def head(filename):
    try:
        with open(filename) as file:
            print(''.join(file.readlines()[:10]))
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ошибка: не задан аргумент командной строки (имя файла).")
    else:
        head(sys.argv[1])
