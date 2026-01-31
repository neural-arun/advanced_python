class User:
    def login(self):
        print("User logged in.")

class Admin(User):
    pass

a = Admin()
a.login()