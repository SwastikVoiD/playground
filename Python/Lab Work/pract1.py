# factoial of a number
# 10-1-2024
# Lab Session
def factorial(x):
    if x == 0 or x == 1:
        return 1
    elif x<0:
        return "factorial cannot be found"
    else:
        return x*factorial(x-1)
a = factorial(10)
print(a)