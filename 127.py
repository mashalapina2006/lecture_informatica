def is_sorted(lst):
    if len(lst) <= 1:
        return True
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1)) or \
           all(lst[i] >= lst[i+1] for i in range(len(lst) - 1))

if __name__ == "__main__":
    nums = []
    while (num := input("Введите число (или Enter): ")):
        try:
           nums.append(float(num))
        except ValueError:
           print("Неверный ввод")
    print("Список отсортирован." if is_sorted(nums) else "Список не отсортирован.")
