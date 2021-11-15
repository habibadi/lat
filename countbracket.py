def countBracket(text):
    stack=[]
    count = 0
    for x in text:
        if x in ["(","{","["]:
            stack.append(x)

        else:
            if not stack:
                count+=1
            else:
                if x == ")":
                    if stack.pop() != "(":
                        count+=1
                if x == "}":
                    if stack.pop() != "{":
                        count+=1
                if x == "]":
                    if stack.pop() != "[":
                        count+=1

    count+=len(stack)
    print(count)


countBracket("(((((()))}")