from students import students

def calculate_percentage(physics_marks,chemistry_marks,biology_marks):
    percentage = (physics_marks + chemistry_marks + biology_marks)/3
    return percentage
highest_percent = 0
topper_name = ""
for student in students:
    name = student["name"]
    

    percentage = round(calculate_percentage(student["Physics"],student["Chemistry"],student["Biology"]),2)
    if percentage > highest_percent:
        highest_percent = percentage
        topper_name = student["name"]

    print(f"{name} has got {percentage}%.")

print(f"The topper of the class is {topper_name} with highest percent of {highest_percent}%.")


