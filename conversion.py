Binary_Number = 1001111
Decimal_value = (1*(2^6)) + (0*(2^5)) + (0*(2^4)) + (1*(2^3)) + (1*(2^2)) + (1*(2^1)) + (1*(2^0))
print(Decimal_value)


# Function to print binary number for the
# input decimal using recursion
def decimalToBinary1(n):
    if (n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary1(n // 2)

    print(n%2, end=' ')



decimalToBinary1(8)
print("\n")


# Function to convert Decimal number
# to Binary number

def decimalToBinary2(n):
	return bin(n).replace("0b","")

print(decimalToBinary2(8))


# Function calculates the decimal equivalent
# to given binary number

def binaryToDecimal(binary):
    decimal, i  = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)

binaryToDecimal(1001)

# Function to convert Binary number
# to Decimal number

def binaryToDecimal2(n):
	return int(n,2)

print(binaryToDecimal2('100'))







