# This method improves complexity of repeated subtraction
# By efficient use of modulo operator in Euclidean algorithm
def getGCD(a, b):
    return b == 0 and a or getGCD(b, a % b)


num1 = -36
num2 = 60

# if user enters negative number, we just changing it to positive
# By definition GCD is the highest positive number that divides both numbers
# -36 & 60 : GCD = 12 (as highest num that divides both)
# -36 & -60 : GCD = 12 (as highest num that divides both)
num1 >= 0 and num1 or -num1
num2 >= 0 and num2 or -num2

print("GCD of", num1, "and", num2, "is", getGCD(num1, num2))