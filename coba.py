def isPalindromRecursive(text, n):
    if(n< len(text)/2):
        indxAwal = n
        indxAkhir = len(text) -n -1
        if (text[indxAwal] == text[indxAkhir]):
            return isPalindromRecursive(text, n + 1)
        elif((64 < ord(text[indxAwal]) < 91) and (96 < ord(text[indxAkhir]) < 123) and (ord(text[indxAwal])+32) == ord(text[indxAkhir])):
            return isPalindromRecursive(text, n + 1)
        elif((96 < ord(text[indxAwal]) < 123) and (64 < ord(text[indxAkhir]) < 91) and (ord(text[indxAwal])-32) == ord(text[indxAkhir])):
            return isPalindromRecursive(text, n + 1)
        else:
            print("No")
            return False
    else:
        print("Yes")
        return True

def isPalindrom(text):
    return isPalindromRecursive(text, 0)


print("\n\nRecursion Example Results")
isPalindrom("lEvel1")