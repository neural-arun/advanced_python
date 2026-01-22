class User:
    def __init__(self,password):
        self.__password = password    # private


u1 = User("secret123")

# ab bahar ki duniya ke liye password exist hi nhi karta.


print(u1.__dict__)