# python ke andar function bhi variable hota hai.

def say_hi():
    print("Hi")

def call_function(func):
    func()     # func is just a variable like any variable which later becomes say_hi in this code block.


call_function(say_hi)