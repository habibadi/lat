def spiral(n,matrix):
    temp = []
    for x in range(1,n+1):
        temp.append(x+(len(matrix)*n))
    matrix.append(temp)

    if len(matrix) < n:
        spiral(n,matrix)
    else:
        print(matrix)


def spirol(n):
    temp = []
    result = []
    for x in range(1,(n*n)+1):
        temp.append(x)
        if x%n == 0:
            result.append(temp)
            temp = []
    print(result)



matrix =[]
spiral(4,matrix)
spirol(4)