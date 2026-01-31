# Debugging: pausing programs and checking it line by line not guessing the error or why program 
# does not run it was suppose to.

def add(a, b):
    result = a + b
    return result       # breakpoint: pause here.

x = 10
y = 20
total = add(x, y)
print(total)
