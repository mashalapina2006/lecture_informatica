numbers = []
while (num := int(input())):
    numbers.append(num)
numbers.sort()
print(*numbers, sep='\n')
