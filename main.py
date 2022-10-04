from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password_list = []


def generate_pass():
    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = pass_letters + pass_symbols + pass_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(
            title="Oops", message="Please fill the empty fields")
        return

    is_ok = messagebox.askokcancel(
        title=website, message=f"Email: {email}\nPassword: {password}\n\nThese credentials will be saved")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "@gmail.com")
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_pass():
    website = website_entry.get()
    message = 'asdfasfd'

    if website == "":
        messagebox.showinfo(
            title="Oops", message="Please enter a website name")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        message = 'No password stored for this site'
    else:
        if website in data:
            message = f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
        else:
            message = 'No password stored for this site'
    finally:
        messagebox.showinfo(title=website, message=message)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
lock_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_pic)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky="w")
email_label = Label(text="Email: ")
email_label.grid(row=2, column=0, sticky="w")
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky="w")

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_btn = Button(text="Search", command=search_pass, width=15)
generate_btn.grid(row=1, column=2, sticky="e")
generate_btn = Button(text="Generate Password", command=generate_pass)
generate_btn.grid(row=3, column=2, sticky="e")
add_btn = Button(text="add", width=46, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
