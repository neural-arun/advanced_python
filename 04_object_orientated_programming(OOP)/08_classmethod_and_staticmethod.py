class Foo:
    @classmethod
    def hi(cls):
        return (cls.__name__)
    

my_object = Foo()
print(my_object.hi())



class PrintHi:
    @staticmethod
    def hi():
        return "I do not take any argument."
    
new_object = PrintHi()

print(new_object.hi())