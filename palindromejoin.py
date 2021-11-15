def joinpal(text):
    textout = ""
    for x in text:
        if x.isalpha():
            textout = textout + x
    textout = textout.lower()
    print(textout)
    for x in range(int(len(textout)/2)):
        if textout[x] != textout[len(textout)-1-x]:
            print(textout[x] , textout[len(textout)-1-x])
            return False
    return True

Input  = "A man, a plan, a canal: Panama"

print(joinpal(Input))