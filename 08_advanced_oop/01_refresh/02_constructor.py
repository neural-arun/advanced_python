class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option


q1 = Question(
    "what is the powerhouse of the cell",
    ["mitochondria", "lysosome", "cytoplasm"],
    "mitochondria"
)
