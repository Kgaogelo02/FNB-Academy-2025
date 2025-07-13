'''
def greet(name):
    print(f"Hello, {name}")
greet("Kgaogelo")

def add(a, b):
    return a + b
result = add(a, b)
print(result)
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")
    
greet("Kgaogelo", "Good Morning")