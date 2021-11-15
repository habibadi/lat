input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = 0
for x in range(2,len(input)):
    for y in range(len(input)+1 - x):
        temp = 0
        for z in range(x):
            temp = temp + input[y+z]
        if temp>result:
            result = temp


print(result)
