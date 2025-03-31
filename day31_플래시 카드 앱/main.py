import tkinter
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
french_words_dict = {}

# data
try:
    french_words_df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    og_data = pd.read_csv("data/french_words.csv")
    french_words_dict = og_data.to_dict(orient="records")
else:
    french_words_dict = french_words_df.to_dict(orient="records")


def push_right_button():
    next_card()
    remove_item()


# random word generate
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(french_words_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(front_card, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(front_card, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(
        card_word, text=current_card["English"], fill="white")


def remove_item():
    french_words_dict.remove(current_card)
    create_df = pd.DataFrame(french_words_dict)
    create_df.to_csv("data/words_to_learn.csv", index=False)


# window
window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# cards
canvas = tkinter.Canvas(
    width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
front_card = canvas.create_image(
    400, 270, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# button
right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(
    image=right_image, highlightthickness=0, command=push_right_button)
right_button.grid(row=1, column=1)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(
    image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
