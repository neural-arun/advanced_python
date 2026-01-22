class Question:
    def __init__(self,text,difficulty):
        self.text = text
        self.difficulty = difficulty

q1 = Question("what is the powerhouse of the cell" , "easy")
q2 = Question("who is the father of chemistry" , "medium")

print(q1.__dict__)
print(q2.__dict__)