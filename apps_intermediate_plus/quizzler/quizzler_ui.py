from quizzler_quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # This "quiz_brain: QuizBrain" means when initialize a new QuizInterface...
        # ...we must pass in quiz_brain object which is of the data type QuizBrain.
        # To do this, we have to import QuizBrain above.

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", padx=20)
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.text_trivia = self.canvas.create_text(
            150,
            125,
            width=280,  # Make this less than the canvas width of 300,
                        # and this width will cause the text to wrap in the canvas.
            text="Test trivia text.",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )

        img_correct = PhotoImage(file="quizzler_images/quizzler_true.png")
        self.button_correct = Button(image=img_correct, highlightthickness=0, padx=20, pady=20, command=self.button_correct_pressed)
        self.button_correct.grid(row=2, column=0)

        img_incorrect = PhotoImage(file="quizzler_images/quizzler_false.png")
        self.button_incorrect = Button(image=img_incorrect, highlightthickness=0, padx=20, pady=20, command=self.button_incorrect_pressed)
        self.button_incorrect.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_trivia, text=q_text)
        else:
            self.canvas.itemconfig(self.text_trivia, text="You've reached the end of the quiz.")
            self.button_correct.config(state="disabled")
            self.button_incorrect.config(state="disabled")

    def button_correct_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def button_incorrect_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
