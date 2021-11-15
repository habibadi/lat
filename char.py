
A = "aaabbccd"
B = 2
crop = []
count = 1
result = ""
for x in range(len(A)-1):
    if A[x] == A[x+1]:
        count+= 1
    else:
        count = 1

    if count == B:
        for z in range(B):
            crop.append(x+1-z)

for y in range(len(A)):
    if y not in crop:
        result =  result + A[y]

print(result)

