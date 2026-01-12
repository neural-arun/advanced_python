class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student("Arun",[89,99,90,89,79])

print(student_one.grades)
print(student_one.name)

student_two = Student("Sarita",[45,78,99,98,100])
print(student_two.name)
print(student_two.grades)
print(student_two.average()) # This tells me average of student two.
print(student_one.average)  # This tells me some wierd things