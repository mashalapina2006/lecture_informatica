def remove_comments(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in lines:
                line = line.split('#', 1)[0].rstrip()  
                outfile.write(line + '\n')
        print(f"Комментарии успешно удалены. Результат сохранен в '{output_file}'.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")
if __name__ == "__main__":
    input_file = input("Введите имя исходного файла: ")
    output_file = input("Введите имя файла для сохранения результата: ")
    remove_comments(input_file, output_file)
