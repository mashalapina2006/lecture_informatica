import string

def pig_latin(text):
    vowels = "aeiou"
    result = []
    for word in text.split():
        punc = ""
        if word and word[-1] in string.punctuation:
            punc = word[-1]
            word = word[:-1]
        if not word:
          result.append(punc)
          continue
        first = word[0]
        word = word.lower()
        if first in vowels:
           translated = word + "way"
        elif any(c in vowels for c in word):
           for i, char in enumerate(word):
              if char in vowels:
                translated = word[i:] + word[:i] + "ay"
                break
        else:
            translated = word + "ay"

        result.append((translated[0].upper() + translated[1:] if first.isupper() else translated) + punc)

    return " ".join(result)

if __name__ == "__main__":
    text = input("Введите строку для перевода на поросячью латынь: ")
    print("Переведенная строка:", pig_latin(text))
