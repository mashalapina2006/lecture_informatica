def pig_latin(text):
    vowels = "aeiou"
    return " ".join(
        (word[1:] + word[0] + "ay" if word[0] not in vowels else word + "way")
        if any(c in vowels for c in word)
        else word + "ay"
        for word in text.split()
    )

if __name__ == "__main__":
    text = input("Введите строку для перевода на поросячью латынь: ")
    print("Переведенная строка:", pig_latin(text))
