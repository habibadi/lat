def longest(input):
    out = ""
    result = 0
    for x in range(len(input)):
        if input[x] in out:
            if len(out) > result:
                result = len(out)
            out = ""
        else:
            out = out + input[x]
    if len(out) > result:
        result = len(out)
    print(result)


Input = ""
longest(Input)

