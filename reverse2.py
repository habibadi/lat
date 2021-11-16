

def reverse(substext):
    if len(substext) == 0:
        return substext
    else:
        return reverse(substext[1:]) + substext[0]

def rever(substext):
    result = ""
    for x in substext:
        result = x + result
    return result


def split(text):
    textArr = text.split()
    for x in range(len(textArr)):
        textArr[x] = rever(textArr[x])
    return " ".join(textArr)


print(split("habib adi astari"))