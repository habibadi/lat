def getstring(text):
    if len(text) > 31:
        print(text[31:text[31:].find("/")+31])

getstring("http://tokopedia.com/discovery/get-this-string/new")