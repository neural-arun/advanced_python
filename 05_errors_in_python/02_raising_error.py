def enter_club(age):
    if age < 18:
        raise ValueError("18 se kam age allowed nahi hai")
    
    print("Welcome to the club 🎉")


enter_club(15)  # yha pr error aayega.

# Another example



def set_password(password):
    if len(password) < 6:
        raise ValueError("Password kam se kam 6 characters ka hona chahiye")
    
    print("Password set ho gaya ✅")


def withdraw(balance, amount):
    # logic likho
    if balance < amount:
        raise ValueError("Not sufficient balance to withdraw this amount.")
    print("Balace withdrawn successfully.")