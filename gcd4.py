def getGCD(a, b):
    return b == 0 and a or getGCD(b, a % b)


num1 = 36
num2 = 60

print("GCD of", num1, "and", num2, "is", getGCD(num1, num2))