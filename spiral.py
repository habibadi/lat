def spiral(n,matrix):
    temp = []
    for x in range(1,n+1):
        temp.append(x+(len(matrix)*n))
    matrix.append(temp)

    if len(matrix) < n:
        spiral(n,matrix)
    else:
        print(matrix)



matrix =[]
spiral(4,matrix)