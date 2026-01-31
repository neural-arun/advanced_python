def deco_name(func):
    def wrapper(*args,**kwargs):
        print("before function")
        func(*args,**kwargs)
        print("after function")
    return wrapper


@deco_name
def say_hi(*names):
    for name in names:
        print(f"Hi {name}")

say_hi("arun", "sarita","uday","sunny")