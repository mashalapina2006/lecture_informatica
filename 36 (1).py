def human_to_dog_age(human_age):
    if human_age < 0:
        return "Ошибка: возраст не может быть отрицательным."
    
    if human_age <= 2:
        return human_age * 10.5
    else:
        return 21 + (human_age - 2) * 4

human_age = float(input("Введите ваш возраст в человеческих годах: "))
dog_age = human_to_dog_age(human_age)
print(f"Возраст собаки в собачьих годах: {dog_age}")

