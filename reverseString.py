def reverseString(text,recursiveText):
    if len(recursiveText) < len(text):
        recursiveText = recursiveText + text[len(text)-len(recursiveText)-1]
        reverseString(text,recursiveText)
    else:
        print(recursiveText)

reverseString("habib","")



