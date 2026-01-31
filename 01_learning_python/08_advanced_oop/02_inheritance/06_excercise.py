class A:
    def greet(self):
        print("Hello")

class B(A):
    def greet(self):
        super().greet()
        print("Hi")
        super().greet()

f1 = B()
f1.greet()