BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 30, "italic")
LANGUAGE_COORDINATES = (400, 150)
WORD_FONT = ("Arial", 60, "bold")
WORD_COORDINATES = (400, 263)
current_card = {}
to_learn = {}


from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("D:\100-Days-of-code-Python\First_21_days\Day_31_Project_-_Flashcards\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# creating a window
window = Tk()
window.title("Flashcards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# importing pictures

card_front_image = PhotoImage(file="/First_21_days/Day_31_Project_-_Flashcards/images/card_front.png")
card_back_image = PhotoImage(file="/First_21_days/Day_31_Project_-_Flashcards/images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", fill='black', font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)


# ------------------------------ DATA ------------------------#


def back_card():
    card_back = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_back.create_image(400, 263, image=card_back_image)
    card_back.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(file="/First_21_days/Day_31_Project_-_Flashcards/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="/First_21_days/Day_31_Project_-_Flashcards/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
