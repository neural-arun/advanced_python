from pathlib import Path

BASE_DIR = Path(__file__).parent

with open(BASE_DIR/"csv.txt","r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines[1:]]


for line in lines:
    person_data = line.split(",")
    name = person_data[0].title()
    age = person_data[1]
    school = person_data[2].capitalize()
    profession = person_data[3].title()
    print(f"{name} is {age} years old and studied in {school} and now is a {profession}.")

#for storing csv data use this format

sample_csv_data = ",".join(person_data)
with open(BASE_DIR/"storing_csv_data.txt" ,"w") as f:
    f.write(sample_csv_data)

