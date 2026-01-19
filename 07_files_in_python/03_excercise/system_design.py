# load questions using questions.txt in a list and clean the list using strip().
from pathlib import Path

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "questions.txt"

with open(file_path,"r") as f:
    question_answer_list = f.readlines()

question_answer_as_dict = {}

for question_answer in question_answer_list:
    question_answer.strip()
    question,answer = question_answer.split("=")
    question_answer_as_dict[question] = int(answer.strip())


marks = 0

for que in question_answer_as_dict:
    user_ans = int(input(f"Answer the question: {que} : "))
    correct_answer = question_answer_as_dict[que]
    if user_ans == correct_answer:
        marks += 1
        print("You got it right.")
        
    else:
        print("Incorrect Answer.")
        
with open(BASE_DIR / "result.txt" , "a") as f:
    f.write(f"Your final score is {marks} / 10")

# ask user question one by one using a for loop in the above dict.


# ask for thier answer 
# check the answer and store it into result.txt
# grade the student "Your final score is {n}/{m} when all the questions are attempted"