print("Hello and Welcome to number guessar game.")
import random
upper_range = (input("Enter the upper range of the number: "))
if upper_range.isdigit():
    upper_range = int(upper_range)
    num_range = (0,upper_range)
else:
    upper_range = int(input("Please enter the upper range in integer format and larger than zero: "))
answer = random.randint(0,upper_range)
print(f"Your range is {num_range} ")

number_of_guesses = 0
while True:
    guess = int(input("Please make a guess: "))
    number_of_guesses += 1
    if guess == answer:
        print("You got it correct!")
        break
    elif guess < answer:
        print("Your guess is smaller than the actual number.")
    else:
        print("Your guess is bigger than the actual number.")
        continue

print(f"You took {number_of_guesses} number of guesses to guess the number")

print("Thanks for playing the game.")
