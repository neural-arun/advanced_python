def total(*args):
    s = 0
    for x in args:
        s += x
    return s

after_addition = total(23,34,56,66)
print(after_addition)

