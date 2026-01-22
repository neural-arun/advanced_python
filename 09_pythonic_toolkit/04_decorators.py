import time

def time_it(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time:", (end - start))
    return wrapper

@time_it
def say_hi():
    print("Hi")

say_hi()