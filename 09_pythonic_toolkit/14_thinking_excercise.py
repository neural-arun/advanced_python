def test():
    yield "A"
    yield "B"
    yield "C"

t = test()

for x in t:
    print(x)

for x in t:
    print(x)
