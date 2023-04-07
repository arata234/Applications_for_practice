from tkinter import *
import pandas as pd
import random
import time
import os


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
THINKING_TIME = 3

try:
    data = pd.read_csv("./flash_card/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./flash_card/data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")

current_word = {}


def next_words():
    global current_word, after_id
    window.after_cancel(after_id)
    current_word = random.choice(word_dict)
    
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    
    after_id = window.after(3000, display_answer)
    
def display_answer():
    global current_word
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")

def is_known():
    word_dict.remove(current_word)
    data = pd.DataFrame(word_dict)
    data.to_csv("./flash_card/data/words_to_learn.csv", index=False)
    if data.empty:
        os.remove("./flash_card/data/words_to_learn.csv")
        window.destroy()
        return
    next_words()

if __name__ == "__main__":
    window = Tk()
    window.title("flash card")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    after_id = window.after(3000, func=display_answer)
    
    back_image = PhotoImage(file="./flash_card/images/card_back.png")
    front_image = PhotoImage(file="./flash_card/images/card_front.png")
    canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas_image = canvas.create_image(400, 264, image=front_image)
    canvas.grid(row=0, column=0, columnspan=2)
    
    title_text = canvas.create_text(400, 150, text="Welcome to", font=(FONT_NAME, 40, "italic"))
    word_text = canvas.create_text(400, 280, text="Flash card", font=(FONT_NAME, 60, "bold"))

    
    # Button
    right_image = PhotoImage(file="./flash_card/images/right.png")
    right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief=FLAT, command=is_known)
    right_button.grid(row=1, column=0)
    
    wrong_image = PhotoImage(file="./flash_card/images/wrong.png")
    wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief=FLAT, command=next_words)
    wrong_button.grid(row=1, column=1)
    
    next_words()
    
    window.mainloop()