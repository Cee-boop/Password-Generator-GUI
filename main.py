from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_field = password_input.get()

    if len(password_field) > 0:
        password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def log_details():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    new_data = {
        website: {
            'email': email,
            'password': password

        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # reading old data:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data:
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # saving updated data:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ----------------------------- LOOKUP SAVED DETAILS ----------------------
def lookup_details():
    website = website_input.get()

    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website['[password']]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops!", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_title = Label(text="Website:", font=('Arial', 14, 'normal'))
website_title.grid(row=1, column=0)
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1)

search_button = Button(text="Search", width=13, command=lookup_details)
search_button.grid(row=1, column=2)


email_username_title = Label(text="Email/Username:", font=('Arial', 14, 'normal'))
email_username_title.grid(row=2, column=0)
email_username_input = Entry(width=35)
email_username_input.insert(0, "chantelle@example.com")
email_username_input.grid(row=2, column=1, columnspan=2)

password_title = Label(text="Password:", font=('Arial', 14, 'normal'))
password_title.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=log_details)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
