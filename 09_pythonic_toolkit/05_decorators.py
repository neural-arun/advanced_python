def decorator_name(func):        # 1️⃣ outer function
    def wrapper():               # 2️⃣ inner function
        # before logic
        func()                   # original function call
        # after logic
    return wrapper               # 3️⃣ return wrapper
