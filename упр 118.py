import string

def is_word_palindrome(text):
    text = text.lower()
    words = [word for word in text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).split()]
    return words == words[::-1]

if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Строка является словесным палиндромом." if is_word_palindrome(text) else "Строка не является словесным палиндромом.")
