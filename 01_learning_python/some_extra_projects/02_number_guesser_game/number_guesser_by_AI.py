import random

print("Hello and Welcome to the Number Guesser Game!")

# --- STEP 1: Get the Range Safe and Sound ---
while True:
    upper_range = input("Enter the upper range of the number: ")
    
    if upper_range.isdigit():
        upper_range = int(upper_range)
        if upper_range > 0:
            break  # We have a valid number, exit the loop!
        else:
            print("Please type a number larger than 0.")
    else:
        print("Invalid input. Please type a number.")

# Now we are safe to set the range variables
num_range = (0, upper_range)
answer = random.randint(0, upper_range)
print(f"Great! I am thinking of a number between 0 and {upper_range}.")

# --- STEP 2: The Game Loop ---
number_of_guesses = 0

while True:
    user_input = input("Please make a guess: ")
    
    # Check if they typed a number BEFORE converting to int
    if user_input.isdigit():
        guess = int(user_input)
    else:
        print("That's not a number! Please try again.")
        continue # Skip the rest of the loop and ask again
        
    number_of_guesses += 1
    
    if guess == answer:
        print("You got it correct!")
        break
    elif guess < answer:
        print("Your guess is smaller than the actual number.")
    else:
        print("Your guess is bigger than the actual number.")

print(f"You took {number_of_guesses} guesses to win.")
print("Thanks for playing!")