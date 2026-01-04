students = [
    {"name":"Arun","grade":95},
    {"name":"Sarita","grade":85},
    {"name":"Uday","grade":75},
    {"name":"sunny","grade":65}
]


for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has got {grade} marks.")