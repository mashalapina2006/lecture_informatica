def main():
    nums = []
    while (s := input("Число или Enter: ")):
        try:
            nums.append(float(s))
        except ValueError:
            print("Неверный ввод")

    if not nums:
        print("Нет чисел")
        return

    avg = sum(nums) / len(nums)
    print(f"Среднее: {avg:.2f}")

    print("\nМеньше среднего:", *[n for n in nums if n < avg] or "Нет", sep="\n")
    print("\nРавны среднему:", *[n for n in nums if n == avg] or "Нет", sep="\n")
    print("\nБольше среднего:", *[n for n in nums if n > avg] or "Нет", sep="\n")

if __name__ == "__main__":
    main()
