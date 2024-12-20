def edit_distance(s, t):
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    
    cost = 0
    if s[-1] != t[-1]:
        cost = 1

    d1 = edit_distance(s[:-1], t) + 1
    d2 = edit_distance(s, t[:-1]) + 1
    d3 = edit_distance(s[:-1], t[:-1]) + cost

    return min(d1, d2, d3)

s = input("Введите первую строку: ")
t = input("Введите вторую строку: ")
distance = edit_distance(s, t)
print(f"Редакционное расстояние между '{s}' и '{t}': {distance}")
