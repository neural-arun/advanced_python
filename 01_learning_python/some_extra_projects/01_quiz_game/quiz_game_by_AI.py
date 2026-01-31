print("Welcome to my quiz game!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    print("Okay, maybe next time!")
    quit()

print("Okay! Let's play :)")
score = 0

# 1. Store all questions in a List of Dictionaries (Data)
# This acts like a mini-database.
quiz_data = [
    {"question": "What is the powerhouse of the cell? ", "answer": "mitochondria"},
    {"question": "What is the functional unit of the kidney? ", "answer": "nephron"},
    {"question": "Which bone is the longest in the human body? ", "answer": "femur"},
    {"question": "What is the energy currency of the cell? ", "answer": "atp"},
    {"question": "Which blood group is the universal donor? ", "answer": "o negative"},
    {"question": "What is the largest gland in the human body? ", "answer": "liver"},
    {"question": "Which pigment gives blood its red color? ", "answer": "hemoglobin"},
    {"question": "What are the 'suicide bags' of the cell? ", "answer": "lysosomes"},
    {"question": "What is the unit of the nervous system? ", "answer": "neuron"},
    {"question": "Which tissue transports water in plants? ", "answer": "xylem"}
]

# 2. The Loop (The Logic Engine)
# We write the game logic ONCE, and it runs for every item in the list.
for item in quiz_data:
    user_answer = input(item["question"]).lower()
    
    if user_answer == item["answer"]:
        print("You got it correct!")
        score += 2
    else:
        print("Incorrect!")
        score -= 1

# 3. Final Results
print(f"Your final score is {score}/{len(quiz_data) * 2}.") 
print(f"Your percentage is {(score / (len(quiz_data) * 2)) * 100}%.")