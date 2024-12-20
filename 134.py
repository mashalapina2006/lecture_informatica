def all_sublists(lst):
    return [lst[i:j] for i in range(len(lst) + 1) for j in range(i, len(lst) + 1)]

if __name__ == "__main__":
    list1 = [1, 2, 3]
    print(f"Подсписки списка {list1}: {all_sublists(list1)}")

    list2 = ['a', 'b', 'c', 'd']
    print(f"Подсписки списка {list2}: {all_sublists(list2)}")

    list3 = [10]
    print(f"Подсписки списка {list3}: {all_sublists(list3)}")

    list4 = []
    print(f"Подсписки списка {list4}: {all_sublists(list4)}")
