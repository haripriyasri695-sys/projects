def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(add(2,3))
print(subtract(5,2))
print(multiply(3,4))
print(divide(10,0))