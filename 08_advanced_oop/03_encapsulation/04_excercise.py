
class User:
    def __init__(self,password):
        self.__password = password    # private

    def change_password(self,old,new):
        if old == self.__password:
            return True
        return False

u1 = User("arun1234")
if u1.change_password("arun1234","sarita1234"):
    print("password changed")
else:
    print("Invalid password.")