def center_string(s, w):
    if len(s) >= w:
        return s  
    else:
        spaces = (w - len(s)) // 2  
        return ' ' * spaces + s 
if __name__ == "__main__":
    test_strings = ["Привет", "Пока", "Кот", "Информатика"]
    widths = [10, 20, 15, 30]

    for s, w in zip(test_strings, widths):
        centered = center_string(s, w)
        print(f"'{centered}' в окне шириной {w}")

