def split(text):
    result = ""
    for x in text.split():
         result = x + " " + result

    return  result

print(split("habib astari adi"))

