def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            outfile.write(f"{line_number}: {line}")

input_file = input("Введите имя исходного файла: ")
output_file = input("Введите имя целевого файла: ")

add_line_numbers(input_file, output_file)
print(f"Файл '{output_file}' успешно создан.")
