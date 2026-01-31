class A:
    def work(self):
        print("A working")

class B(A):
    def work(self):
        print("B working")

objs = [A(), B()]

for o in objs:
    o.work()
