def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = gen()
# print(next(g))
# print(next(g))
# print(next(g))  # StopIterationError

for x in gen():
    print(x)