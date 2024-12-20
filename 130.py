import re

tokenize = lambda expression: re.findall(r"(\d+|\+|\-|\*|\/|\^|\(|\))", expression)

def mark_unary_operators(tokens):
    result = tokens[:]
    for i, token in enumerate(tokens):
        if token in ('+', '-') and (i == 0 or tokens[i-1] in '+-*/^('):
            result[i] = 'u' + token
    return result

if __name__ == "__main__":
    expression = input("Введите выражение: ")
    tokens = tokenize(expression)
    marked_tokens = mark_unary_operators(tokens)
    print("Исходный список лексем:", tokens)
    print("Список лексем с помеченными унарными операторами:", marked_tokens)
