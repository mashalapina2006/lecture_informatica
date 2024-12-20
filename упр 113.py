words = []
while True:
    word = input("Введите слово (или нажмите Enter для завершения): ")
    if not word:
        break
    words.append(word)

unique_words = []
for word in words:
  if word not in unique_words:
    unique_words.append(word)

for word in unique_words:
  print(word)
