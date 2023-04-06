from tkinter import *
from tkinter import messagebox
import json
import string
import secrets


def find_password():
    website = website_entry.get().upper()
    try:
        with open("./tkinter_tutorial/password.json") as f:
            data = json.load(f)
            
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")
        
    else: 
        if website in data:
            id = data[website]["ID"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {id}\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")

# generate random password
def generate_password():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(secrets.choice(chars) for _ in range(15)))

# save password
def save_password():
    if len(website_entry.get()) > 0 and len(password_entry.get()) > 0:
        data = {website_entry.get().upper(): 
            {"ID": ID_entry.get(), "password": password_entry.get()}}
        
        with open("./tkinter_tutorial/password.json", "r") as f:
            d = json.load(f)
            
        web = website_entry.get().upper()
        is_registered = d.get(web, False)
        
        if is_registered == False:
            is_ok = messagebox.askokcancel("Password Manager", f"Save password OK?\n Email: {data[web]['ID']}\n Password: {data[web]['password']}")
            if is_ok == False:
                return
            
            d.update(data)
            with open("./tkinter_tutorial/password.json", "w") as f:
                json.dump(d, f)
                website_entry.delete(0, END)
                password_entry.delete(0, END)    
        
        else:
            
            ID_entry.delete(0, END)
            password_entry.delete(0, END) 
            ID_entry.insert(0, is_registered["ID"])
            password_entry.insert(0, is_registered["password"])
    
    else:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty")

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
website_entry = Entry(width=25, relief=GROOVE, bd=2)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)

ID_entry = Entry(width=45, relief=GROOVE, bd=2)
ID_entry.grid(row=2, column=1, columnspan=2, sticky=W)

password_entry = Entry(width=25, relief=GROOVE, bd=2)
password_entry.grid(row=3, column=1, sticky=W)


#button
generate_password_button = Button(text="Generate Password", width=15, relief=GROOVE, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=W)

add_button = Button(text="add", width=38, relief=GROOVE, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

search_button = Button(text="Search", width=15, relief=GROOVE, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()