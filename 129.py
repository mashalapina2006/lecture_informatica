import re

def tokenize(expression):
    """
    Разбивает математическое выражение на лексемы.

    Args:
        expression: Строка, содержащая математическое выражение.

    Returns:
        Список лексем (операторов, чисел и скобок).
    """
    return re.findall(r"(\d+|\+|\-|\*|\/|\^|\(|\))", expression)


if __name__ == "__main__":
    expression = input("Введите математическое выражение: ")
    tokens = tokenize(expression)
    print("Список лексем:", tokens)
