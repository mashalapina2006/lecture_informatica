def find_longest_word(input_file):
    with open(input_file) as infile:
        words = infile.read().split()
    if words:
        longest_word = max(words, key=len)
        print(longest_word, len(longest_word))
    else:
        print("Файл пуст.")
input_file = input("Введите имя файла: ")
find_longest_word(input_file)
