

def reverse(substext):
    if len(substext) == 0:
        return substext
    else:
        return reverse(substext[1:]) + substext[0]



def split(text):
    textArr = text.split()
    for x in range(len(textArr)):
        textArr[x] = reverse(textArr[x])
    return " ".join(textArr)


print(split("habib adi astari"))