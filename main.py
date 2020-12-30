from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
converted_data = {}

try:
    csv_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    converted_data = original_data.to_dict(orient="records")
else:
    converted_data = csv_data.to_dict("records")


def generate_random_word_from_csv_file():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(converted_data)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_text,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_text,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    converted_data.remove(current_card)
    data = pandas.DataFrame(converted_data)
    data.to_csv("data/words_to_learn.csv")
    generate_random_word_from_csv_file()


window = Tk()
window.title("Flashcard Language Learning Application")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(False, False)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=generate_random_word_from_csv_file)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

generate_random_word_from_csv_file()

window.mainloop()



