import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):   # type hint
        self.quiz = quiz_brain

        # window
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # canvas
        self.canvas = tkinter.Canvas(height=250, width=300)
        self.quiz_text = self.canvas.create_text(
            150,
            130,
            width=280,  # 텍스트 폭 지정
            text="quiz_text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # button
        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(
            image=true_img,
            highlightthickness=0,
            command=self.answer_true
            )
        self.true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(
            image=false_img,
            highlightthickness=0,
            command=self.answer_false
            )
        self.false_button.grid(row=2, column=1)

        # label
        self.score_text = tkinter.Label(
            text=f"score: {self.quiz.score}",
            background=THEME_COLOR,
            foreground="white"
            )
        self.score_text.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
