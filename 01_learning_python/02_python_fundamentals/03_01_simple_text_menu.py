user_input = input("Type 'p' to print or Type 'q' to quit: ")

while user_input == "p":
    print("Hello")
    user_input = input("Type 'p' to print or Type 'q' to quit: ")
    if user_input == "q":
        print("Now we are quitting the program.")
