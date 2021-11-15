def coutlast(text):
    textArr = text.split()
    if len(textArr) > 1:
        return len(textArr[len(textArr)-1])
    else:
        return 0

print(coutlast("habib Astari Adi"))
