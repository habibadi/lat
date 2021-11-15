def numss(input,target):
    vol = 0
    for x in range(len(input)):
        for y in range(x+1,len(input)):
            if input[x] < input[y]:
                temp = input[x]*(y-x)
                if temp>vol:
                    vol = temp
            else:
                temp = input[y]*(y-x)
                if temp>vol:
                    vol = temp
    print(vol)

nums = [1,8,6,2,5,4,8,3,7]
target = 6
numss(nums,target)