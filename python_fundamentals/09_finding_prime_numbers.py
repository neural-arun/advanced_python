for n in range(2,102):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} is not a prime number because n = {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")
