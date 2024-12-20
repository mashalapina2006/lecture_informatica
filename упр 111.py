numbers = []
while (num := int(input())):
    numbers.append(num)
numbers.sort(reverse=True)
print(*numbers, sep='\n')
