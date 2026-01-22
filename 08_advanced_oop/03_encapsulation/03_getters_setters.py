# how do we use the private password.
# here comes the getters and setters.


class User:
    def __init__(self,password):
        self.__password = password    # private

    def check_password(self,input_password):
        return input_password == self.__password


u1 = User("secret123")
print(u1.check_password("secret123"))   # True

print(u1.check_password("wrong"))  # FAlse

print(u1._User__password)  # ye nahi kiya jata hai.