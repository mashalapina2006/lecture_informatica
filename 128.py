def countRange(lst, min_val, max_val):
    return sum(1 for num in lst if min_val <= num < max_val)


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Список: {list1}")
    print(f"Количество элементов от 3 до 7: {countRange(list1, 3, 7)}")
    print(f"Количество элементов от 1 до 10: {countRange(list1, 1, 10)}")
    print(f"Количество элементов от 5 до 100: {countRange(list1, 5, 100)}")
    print(f"Количество элементов от 0 до 2: {countRange(list1, 0, 2)}")

    list2 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1]
    print(f"\nСписок: {list2}")
    print(f"Количество элементов от 3 до 8: {countRange(list2, 3, 8)}")
    print(f"Количество элементов от 1 до 11: {countRange(list2, 1, 11)}")
    print(f"Количество элементов от 5 до 100: {countRange(list2, 5, 100)}")
    print(f"Количество элементов от 0 до 2: {countRange(list2, 0, 2)}")

    list3 = [1, 2.5, 3, 4.7, 5, 6.1, 7, 8.2, 9, 10.5]
    print(f"\nСписок: {list3}")
    print(f"Количество элементов от 3 до 8: {countRange(list3, 3, 8)}")
    print(f"Количество элементов от 1 до 11: {countRange(list3, 1, 11)}")
    print(f"Количество элементов от 5 до 100: {countRange(list3, 5, 100)}")
    print(f"Количество элементов от 0 до 2: {countRange(list3, 0, 2)}")
