def my_decorator(my_func):
    def wrapper():
        print("before function.")
        my_func()
        print("after function.")
    return wrapper
# decorator wrapper function return karta hai.

def say_hi():
    print("Hi")

say_hi = my_decorator(say_hi)
my_decorator(my_func=say_hi())

# now there is a shortcut for this

# just put the @my_decorator at the top of say_hi() function. output will be same.