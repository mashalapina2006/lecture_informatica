example_list = [1, [2, 3], [4, [5, 6]], 7, 8, [9, 10]]
example_list_2 = [[1, 2], 3, [4, [5]], 6]
example_list_3 = []

flatten = lambda data: (
    [] if not data else 
    flatten(data[0]) + flatten(data[1:]) if isinstance(data[0], list) else 
    [data[0]] + flatten(data[1:])
)

print(flatten(example_list))
print(flatten(example_list_2))
print(flatten(example_list_3))
