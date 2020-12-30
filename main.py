from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"


def generate_random_word_from_csv_file():
    csv_data = pandas.read_csv("data/french_words.csv")
    data = pandas.DataFrame(csv_data)
    converted_data = data.to_dict("records")
    current_card = random.choice(converted_data)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_text,text=current_card["French"])


window = Tk()
window.title("Flashcard Language Learning Application")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(False, False)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=generate_random_word_from_csv_file)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=generate_random_word_from_csv_file)
known_button.grid(row=1, column=1)

generate_random_word_from_csv_file()

window.mainloop()



