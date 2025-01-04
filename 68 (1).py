def letter_grade_to_numeric(grade):
    grades_dict = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'D-': 0.7,
        'F': 0.0
    }
    return grades_dict[grade]
def calculate_average_grade():
    total_score = 0
    count = 0
    
    while True:
        grade = input("Введите оценку (или нажмите Enter для завершения): ").strip()
        
        if grade == "":
            break
        
        total_score += letter_grade_to_numeric(grade)
        count += 1
    
    if count > 0:
        average_score = total_score / count
        print(f"Средняя оценка: {average_score:.1f}")
    else:
        print("Не введено ни одной оценки.")

calculate_average_grade()
