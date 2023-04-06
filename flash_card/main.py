from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
IS_ENGLISH = True

word_df = pd.read_csv("C:/Users/arata/OneDrive/ドキュメント/GitHub/Applications_for_practice/flash_card/data/french_words.csv")
word_dict = word_df.to_dict()
print(word_dict)

def change_words():
    pass


if __name__ == "__main__":
    window = Tk()
    window.title("flash card")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    
    # back_image = PhotoImage(file="./flash_card/images/card_back.png")
    # bg_canvas = Canvas(width=900, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
    # bg_canvas.create_image(400, 264, image=back_image)
    # bg_canvas.grid(row=0, column=0, columnspan=2, rowspan=2)
    
    front_image = PhotoImage(file="./flash_card/images/card_front.png")
    ft_canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
    ft_canvas.create_image(400, 264, image=front_image)
    ft_canvas.grid(row=0, column=0, columnspan=2)
    
    #Label
    title_label = Label(text="Welcome to", font=(FONT_NAME, 40, "italic"))
    title_label.config(bg="white")
    title_label.place(x=400, y=150, anchor=CENTER)
    
    word_label = Label(text="Flash card", font=(FONT_NAME, 60, "bold"))
    word_label.config(bg="white")
    word_label.place(x=400, y=280, anchor=CENTER)
    
    
    
    # Button
    right_image = PhotoImage(file="./flash_card/images/right.png")
    right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief=FLAT)
    right_button.grid(row=1, column=0)
    
    wrong_image = PhotoImage(file="./flash_card/images/wrong.png")
    wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, relief=FLAT)
    wrong_button.grid(row=1, column=1)
    
    
    
    
    window.mainloop()