class Question:
    def __init__(self, text: str, options: list[str], correct_option_index: int):
        self.text = text
        self.options = options
        self.correct_option_index = correct_option_index


class Cinquiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
