import string

def remove_punctuation(text):
    return ''.join(c if c not in string.punctuation else ' ' for c in text).split()

if __name__ == "__main__":
    text = input("Введите строку: ")
    words = remove_punctuation(text)
    print("Список слов:", words)
