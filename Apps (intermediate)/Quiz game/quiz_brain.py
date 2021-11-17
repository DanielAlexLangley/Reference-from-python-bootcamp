
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0  # so that all our quizzes start from first question
        self.question_list = q_list
        self.score = 0
        # this is the list of questions, which will be passed to QuizBrain object when it's initialized

    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # checks if true or false, then returns the answer

    def next_question(self):
        # this method should pull up question from questions_list depending on which question we're on
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True or false?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
