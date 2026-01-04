print("Welxome to my quiz game!")

is_user_playing = input("Do you want to take a quiz? ").lower()

if is_user_playing != "yes":
    print("Thanks for visiting.")
else:
    score = 0
    answer = input("What is the powerhouse of the cell? ").lower()

    if answer == "mitochondria":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1

    
    answer = input("What is the functional unit of the kidney? ").lower()

    if answer == "nephron":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1

    
    answer = input("Which bone is known as the longest in the human body? ").lower()

    if answer == "femur":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1

    
    answer = input("What is the energy currency of the cell? ").lower()

    if answer == "atp":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1

    
    answer = input("Which blood group is known as the universal donor? ").lower()

    if answer == "o negative":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1

    
    answer = input("What is the largest gland in the human body? ").lower()

    if answer == "liver":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1

   
    answer = input("Which pigment gives blood its red color? ").lower()

    if answer == "hemoglobin":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1


    answer = input("What are the 'suicide bags' of the cell called? ").lower()

    if answer == "lysosomes":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1


 
    answer = input("What is the structural and functional unit of the nervous system? ").lower()

    if answer == "neuron":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1


    answer = input("Which tissue transports water in plants? ").lower()

    if answer == "xylem":
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1


print(f"Your final score is {score}/20.")
print(f"Your percentage is {(score/20)*100}%.")

print("Thanks for taking the quiz.")



# learning: do not repeat yourself.