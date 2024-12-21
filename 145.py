def calculate_score(word):
    
    letter_scores = {
        'А': 2, 'Б': 3, 'В': 4, 'Г': 3, 'Д': 2,
        'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 3, 'И': 1,
        'Й': 3, 'К': 4, 'Л': 2, 'М': 4, 'Н': 1,
        'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1,
        'У': 2, 'Ф': 8, 'Х': 5, 'Ц': 4, 'Ч': 5,
        'Ш': 5, 'Щ': 8, 'Ъ': 10, 'Ы': 2, 'Ь': 2,
        'Э': 10, 'Ю': 10, 'Я': 10
    }
    
    score = 0
    for letter in word.upper():         score += letter_scores.get(letter, 0) 
    
    return score


word = input("Введите слово: ")
score = calculate_score(word)

print(f"Слово '{word}' приносит {score} очков.")
