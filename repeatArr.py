arr = [3, 4 ,1, 4 ,1]

countArr = dict()
out = 0
result = 0

for x in arr:
    if x in countArr:
        countArr[x] += 1
    else:
        countArr[x] = 1

for key in countArr:
    if countArr[key] > out:
        out = countArr[key]
        result = key


print(result)
