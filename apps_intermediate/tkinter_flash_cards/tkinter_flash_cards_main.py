
import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}

try:
    data = pandas.read_csv("tkinter_flash_cards_data/tkinter_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("tkinter_flash_cards_data/tkinter_flash_cards_french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def user_knows():
    global CURRENT_CARD
    to_learn.remove(CURRENT_CARD)
    new_dict = pandas.DataFrame(to_learn)
    new_dict.to_csv("tkinter_flash_cards_data/tkinter_words_to_learn.csv", index=False)
    next_card()


def next_card():
    global CURRENT_CARD, flip_timer
    window.after_cancel(flip_timer)
    CURRENT_CARD = random.choice(to_learn)
    canvas.itemconfig(card_image, image=img_card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=CURRENT_CARD["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)
    print(CURRENT_CARD)
    print(to_learn)


def flip_card():
    global CURRENT_CARD
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=CURRENT_CARD["English"], fill="white")
    canvas.itemconfig(card_image, image=img_card_back)


window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(1000, func=flip_card)

img_card_front = tkinter.PhotoImage(file="tkinter_flash_cards_images/tkinter_flash_cards_card_front.png")
img_card_back = tkinter.PhotoImage(file="tkinter_flash_cards_images/tkinter_flash_cards_card_back.png")

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_image = canvas.create_image(400, 263, image=img_card_front)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text='', anchor='n', font=("Ariel", 40, "italic"), fill='black')
card_word = canvas.create_text(400, 263, text="", anchor='n', font=("Ariel", 60, "bold"), fill='black')

button_wrong_img = tkinter.PhotoImage(file="tkinter_flash_cards_images/tkinter_flash_cards_wrong.png")
button_wrong = tkinter.Button(image=button_wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1, columnspan=1)

button_right_img = tkinter.PhotoImage(file="tkinter_flash_cards_images/tkinter_flash_cards_right.png")
button_right = tkinter.Button(image=button_right_img, highlightthickness=0, command=user_knows)
button_right.grid(column=1, row=1, columnspan=1)

next_card()

window.mainloop()
