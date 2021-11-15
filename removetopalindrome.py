a = "abbga"
isPalindrome = False

for x in range(len(a)-1):
    b =  a[:x] + a[x+1:]

    for x in range(int(len(b)/2)):
        if b[x] != b[len(b)-1-x]:
            isPalindrome = False
            break
        elif x == int(len(b)/2)-1 :
            isPalindrome = True

    if isPalindrome :
        break


print(isPalindrome)





