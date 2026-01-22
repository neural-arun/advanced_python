class User:
    def __init__(self,password):
        self.password = password


u1 = User("secret123")
u1.password  =  "hacked" # aise koi bhi password change kar sakta hai.

print(u1.password)


