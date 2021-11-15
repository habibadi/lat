def pair(arr,num):
    out = []
    temp =[0,0]
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            print(arr[x],arr[y])
            if arr[x] + arr[y] == num:
                temp[0] = arr[x]
                temp[1] = arr[y]
                out.append(temp)

    if len(out)>0:
        print(out)
    else:
        print("tidak ada")


A = [0, -1, 2, -3, 1]
x = -2
pair(A,x)

