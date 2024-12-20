def is_sublist(larger, smaller):
    if not smaller:
        return True
    return any(larger[i:i+len(smaller)] == smaller for i in range(len(larger) - len(smaller) + 1))

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 3]
    list3 = [1, 5]
    list4 = []
    list5 = [1, 2, 3, 4, 5]
    list6 = [4,5,6]
    list7 = [5]

    print(f"Is {list2} a sublist of {list1}? {is_sublist(list1, list2)}")
    print(f"Is {list3} a sublist of {list1}? {is_sublist(list1, list3)}")
    print(f"Is {list4} a sublist of {list1}? {is_sublist(list1, list4)}")
    print(f"Is {list1} a sublist of {list1}? {is_sublist(list1, list5)}")
    print(f"Is {list6} a sublist of {list1}? {is_sublist(list1, list6)}")
    print(f"Is {list7} a sublist of {list1}? {is_sublist(list1, list7)}")
