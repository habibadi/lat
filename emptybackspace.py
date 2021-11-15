def samecak(s,t):
    outS = ""
    outT = ""
    count = 0
    for x in range(len(s)):
        if s[len(s)-1-x] != "#" and count == 0:
            outS = s[len(s)-1-x] + outS
        elif s[len(s)-1-x] == "#":
            count += 1
        elif count > 0:
             count -=1

    count = 0
    for x in range(len(t)):
        if t[len(t)-1-x] != "#" and count == 0:
            outT = s[len(t)-1-x] + outT
        elif t[len(t)-1-x] == "#":
            count += 1
        elif count > 0:
             count -=1
    print(outS,outT)
    if len(outS) == len(outT):
        for x in range(len(outS)):
            if outS[x] != outT[x]:
                return False

        return True

s = "ab##"
t = "c#d#"

print(samecak(s,t))