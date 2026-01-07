avg  = lambda seq : sum(seq) / len(seq)

total = sum

top_marks = max

operation_functions = {
    "average" : avg,
    "total" : total,
    "maximum mark" : top_marks
}

students = [
    {"name": "Arun", "grades": [45,67,89,88,66,44]},
    {"name": "sunny", "grades": [1,2,3,4,5,6,7]},
    {"name": "Uday", "grades": [3,6,78,9,0,5,54]},
    {"name": "Sarita", "grades": [45,56,76,78,89,45]},
    {"name": "Ayush", "grades": [34,45,76,56,78,34]}
]

for student in students:
    grades = student["grades"]
    print(f"{student["name"]}")
    operation = input("Type 'average/total/maximum mark? ")
    result = operation_functions[operation]
    print(result(grades))
