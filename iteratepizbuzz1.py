def fizzBuzz(n):

    if n > -1:
        n=n-1
        fizzBuzz(n)

        if (n+1)%3 == 0:
            if (n+1)%5 == 0:
                print("Hello-Boy")
            else:
                print("Hello")
        elif (n+1)%5 == 0:
            print("Boy")
        else:
            print((n+1))


fizzBuzz(100)

