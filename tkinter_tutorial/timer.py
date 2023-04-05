from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# timer reset

# timer mexhanism

# countdown mechanism

# UI setup


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)


canvas = Canvas(window, height=224, width=200)
tomato_image = PhotoImage(file="./tkinter_tutorial/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(103, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.pack()



window.mainloop()