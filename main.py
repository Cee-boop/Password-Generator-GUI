from tkinter import *
from tkinter import messagebox
import random
import pyperclip


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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                        f"\nPassword: {password} \nIs it OK to save?")
        if is_ok:
            with open("./data.txt", mode='a') as data_file:
                log = f"{website} | {email} | {password}\n"
                data_file.write(log)
                website_input.delete(0, END)
                password_input.delete(0, END)


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
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

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
