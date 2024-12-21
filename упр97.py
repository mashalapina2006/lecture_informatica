def precedence(operator):
    if operator == '+':
        return 1
    elif operator == '-':
        return 1
    elif operator == '*':
        return 2
    elif operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return -1
if __name__ == "__main__":
    user_input = input("Введите оператор (+, -, *, /, ^): ") 
    result = precedence(user_input)
    if result != -1:
        print(f"Приоритет оператора '{user_input}': {result}")
    else:
        print("Ошибочный ввод оператора.")

