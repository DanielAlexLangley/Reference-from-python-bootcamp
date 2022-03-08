
# This converts string data into object which now has all of that data in easy and foolproof way of accessing it.

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
