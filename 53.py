def num_to_letter(grade):
    if grade >= 4.0:
        return "A+"
    elif 3.7 <= grade < 4.0:
        return "A"
    elif 3.3 <= grade < 3.7:
        return "A-"
    elif 3.0 <= grade < 3.3:
        return "B+"
    elif 2.7 <= grade < 3.0:
        return "B"
    elif 2.3 <= grade < 2.7:
        return "B-"
    elif 2.0 <= grade < 2.3:
        return "C+"
    elif 1.7 <= grade < 2.0:
        return "C"
    elif 1.3 <= grade < 1.7:
        return "C-"
    elif 1.0 <= grade < 1.3:
        return "D"
    else:
        return "F"
grade_input = float(input("Введите вашу числовую оценку: "))
letter_grade = num_to_letter(round(grade_input, 1))
print("Ваша буквенная оценка: ", letter_grade)
