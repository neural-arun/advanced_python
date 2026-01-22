class User:
    def __init__(self, email):
        self.email = email

class Admin(User):
    def __init__(self,email,level):
        super().__init__(email)
        self.level = level