# Program to check if a number is prime or not

def isPrimeNumber(N):
    isPrime = True
    for i in range(2, N):
        if (N % i) == 0:
            isPrime = False
            break
    return isPrime

def checkNumber(N):
    out = 0
    if N > 3:
        for x in range(4,N+1):
            if not isPrimeNumber(x) and x%6 != 0:
                out= out+x
            print(x, out)
    return out

print(checkNumber(15))
