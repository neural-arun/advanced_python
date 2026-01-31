# Using inheritance to extend a class

class Student:
    def __init__(self,name,school):
        self.name = name
        self.school_name = school
        self.marks = []

    def average(self):
        if not self.marks:
            return None
        return sum(self.marks) / len(self.marks)
    

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary

    @property  # Changes a method with no parameter to a property.
    def weakly_salary(self):
        return self.salary / 4

arun = WorkingStudent("Arun","Shishu mandir vidyalaya",90000)

print(arun.salary)
 # Function hai to isko call bhi karna hoga.

if arun.average() == None:
    print("No marks available")
else:
    print(arun.average())
print(arun.weakly_salary)  # if i had not put @property up there above fuctions i would have to
# put a bracket after arun.salary like this arun.salary()
print(arun.name)
print(arun.school_name)
