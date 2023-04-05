import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    new_text = inp.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="click me", command=button_clicked)
button.grid(row=1, column=1)

button2 = tkinter.Button(text="new button")
button2.grid(row=0, column=2)

inp = tkinter.Entry(width=10)
inp.grid(row=2, column=3)









window.mainloop()