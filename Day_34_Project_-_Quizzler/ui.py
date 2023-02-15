from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, question_text: QuizBrain):
        self.question_text = question_text
        self.window=Tk()
        self.window.title("Quizzler")
        #self.window.minsize(width=400, height=600)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quote_text = self.canvas.create_text(150,
                                                  125,
                                                  width=280,
                                                  text="some question goes here",
                                                  font=("Arial", 15, "italic"),
                                                  fill=THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="D:/100-Days-of-code-Python/Day_34_Project_-_Quizzler/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_chosen)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="D:/100-Days-of-code-Python/Day_34_Project_-_Quizzler/images/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_chosen)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.question_text.still_has_questions():
            self.score_label.config(text=f"Score: {self.question_text.score}")
            q_text = self.question_text.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_chosen(self):
        self.give_feedback(self.question_text.check_answer("True"))

    def false_chosen(self):
        is_right = self.question_text.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg='red')
        self.window.after(300, self.get_next_question)