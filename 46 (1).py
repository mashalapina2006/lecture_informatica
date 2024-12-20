def cell_color(coords):
    col = ord(coords[0].lower()) - ord('a')
    row = int(coords[1]) - 1
    return "белая" if (col + row) % 2 == 0 else "черная"

while True:
    coords = input("Координаты (или 'quit'): ")
    if coords.lower() == 'quit':
        break
    print(f"Клетка {coords} - {cell_color(coords)}.")
