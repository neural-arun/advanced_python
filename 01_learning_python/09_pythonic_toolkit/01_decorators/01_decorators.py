def greet():
    print("hi")

greet()

# now if we want to print something before and after function like this

def greet():
    print("before function")
    print("Hi")
    print("after function")

# now if we have to do this for each function we then code becomes repetetive.

# Base of decorators.

# function ke andar function
def outer():
    def inner():
        print("hi from inner")
    inner()

outer()
