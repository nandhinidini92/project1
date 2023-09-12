# Recursive function to return GCD of two number
def findGCD(num1, num2):
    
    # Everything divides 0
    if num1 == 0 or num2 == 0:
        return num1 + num2
    
    # base case
    if num1 == num2:
        return num1
    
    # num1>num2
    if num1 > num2:
        return findGCD(num1 - num2, num2)
    else:
        return findGCD(num1, num2 - num1)


num1 = 36
num2 = 60

print("GCD of", num1, "and", num2, "is", findGCD(num1, num2))