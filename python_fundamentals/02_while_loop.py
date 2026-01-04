is_learning = True

while is_learning:
    print("It is good that you are learning.")
    user_input = input("Are you still learning? ")
    if user_input == "yes":
        is_learning = True
    else:
        is_learning = False


print("Now we are quittin the program.")