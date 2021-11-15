def recursiveLoop(num):
    if num > 0:
        num = num - 1
        recursiveLoop(num)
        print(num+1)

recursiveLoop(5)
