
#add(a, b) that adds two numbers a and b
#subtract(a, b) that subtracts two numbers a and b
#multiply(a, b) that multiplies two numbers a and b
#divide(a, b) that divides two numbers a and b
#exp(a, b) that takes a to the exponent (or power) of b

def add(a,b):
    answer = a + b
    return answer
def subtract(a,b):
    answer = a - b
    return answer
def multiply(a,b):
    answer = a * b
    return answer
def divide(a,b):
    answer = a // b
    return answer
def exponent(a,b):
    answer = a ** b
    return answer

print(add(10, 11))
print(subtract(100, 975))
print(multiply(12, 9))
print(divide(299, 8))
print(exponent(22, 5))