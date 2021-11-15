def numss(input,target):
    out = []
    for x in range(len(input)):
        for y in range(x+1,len(input)):
            if input[x]+input[y] == target:
                out.append(input[x])
                out.append(input[y])
    print(out)

nums = [3,2,4]
target = 6
numss(nums,target)
