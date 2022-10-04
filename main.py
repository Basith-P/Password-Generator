from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, "@gmail.com")
        password_entry.delete(0, END)
        website_entry.focus()

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
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_btn = Button(text="Generate Password")
generate_btn.grid(row=3, column=2, sticky="e")
add_btn = Button(text="add", width=46, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")


window.mainloop()
