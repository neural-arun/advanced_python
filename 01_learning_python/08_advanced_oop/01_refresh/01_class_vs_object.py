class Question():
    pass

q1 = Question()

q1.text = "what is the powerhouse of the cell"
q1.options = ["mitochondria","lysosome","cytoplasm"]
q1.correct_option = "mitochondria"

print(q1.__dict__)