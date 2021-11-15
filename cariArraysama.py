
A = ["abab", "ab", "ebcd"]

def myFucn(e):
    return len(e)


A.sort(key=myFucn)
out = ""
#print(len(A[0]))
for x in range(len(A[0])):
    isSameChar = True
    #print("AAAAA")
    for y in range(len(A) - 1):
        #print(A[y][x], A[y + 1][x])
        if A[y][x] != A[y + 1][x]:
            isSameChar = False
            break

    if isSameChar:
        out = out + A[0][x]

    else:
        break
print(out)