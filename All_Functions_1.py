import math

# Add, Subtract, multiply, divide, prime number & Even number functions defined
def addNumbers(a, b):
    print("Sum is ", a + b)

def subtractNumbers(a, b):
    print("Difference is ", a-b)

def multiplyNumbers(a, b):
    print("Product is ", a * b)

def divideNumbers(a, b):
    print("Division is ", a / b)

def is_prime(a):
    '''Check if num is prime or not.'''
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True

def is_even(x):
    if x % 2 == 0:
        return True
        print("Even",x)
    else:
        return False
        print("ODD",x)