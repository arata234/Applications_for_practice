from tkinter import *



# generate random password
def generate_password():
    pass

# save password
def save_password():
    data = {f"{website_entry.get()}": 
        {"ID": ID_entry.get(), "password": password_entry.get()}}
    for k, v in data.items():
        print(k, v)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50, bg="white")

canvas = Canvas(window, width=159, height=175, bg='white', highlightthickness=0)
key_image = PhotoImage(file="./tkinter_tutorial/key.png")
canvas.create_image(80, 86, image=key_image)
canvas.grid(row=0, column=1)


#label
web_label = Label(text="Website: ", bg="white")
web_label.grid(row=1, column=0)

ID_label = Label(text="Email/Username: ", bg="white")
ID_label.grid(row=2, column=0)

password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)


#entry
website_entry = Entry(width=45, relief=GROOVE, bd=2)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)

ID_entry = Entry(width=45, relief=GROOVE, bd=2)
ID_entry.grid(row=2, column=1, columnspan=2, sticky=W)

password_entry = Entry(width=25, relief=GROOVE, bd=2)
password_entry.grid(row=3, column=1, sticky=W)


#button
generate_password_button = Button(text="Generate Password", width=15, relief=GROOVE)
generate_password_button.grid(row=3, column=2, sticky=W)

add_button = Button(text="add", width=38, relief=GROOVE, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()