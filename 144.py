import string

def clean_string(s):
   
    return ''.join(c.lower() for c in s if c.isalnum())

def are_anagrams(phrase1, phrase2):
 
    return sorted(clean_string(phrase1)) == sorted(clean_string(phrase2))


phrase1 = input("Введите первую фразу: ")
phrase2 = input("Введите вторую фразу: ")

if are_anagrams(phrase1, phrase2):
    print(f'"{phrase1}" и "{phrase2}" являются анаграммами.')
else:
    print(f'"{phrase1}" и "{phrase2}" не являются анаграммами.')
