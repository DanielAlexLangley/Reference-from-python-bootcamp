
from tkinter import messagebox  # This is a module (not a class) and must be imported separately
import pyperclip
import tkinter
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.delete(0, 'end')
    entry_password.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    string_website = entry_website.get()
    string_email_username = entry_email_username.get()
    string_password = entry_password.get()

    new_data = {
        string_website: {
            "email": string_email_username,
            "password": string_password,
        }
    }

    if len(string_website) == 0 or len(string_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=string_website, message=f"These are the details entered: \nEmail: "
                                                                     f"{string_email_username} \nPassword: "
                                                                     f"{string_password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("tkinter_pw_manager_passwords.json", "r") as data_file:
                    data = json.load(data_file)  # This reads the old json data.
            except(FileNotFoundError, json.decoder.JSONDecodeError):
                with open("tkinter_pw_manager_passwords.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)  # This saves the new json data.
            else:
                data.update(new_data)  # This updates the old data with the new data.
                with open("tkinter_pw_manager_passwords.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_password.delete(0, 'end')
                entry_website.delete(0, 'end')


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    string_website = entry_website.get()
    try:
        with open("tkinter_pw_manager_passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("tkinter_pw_manager_passwords.json", "w") as data_file:
            messagebox.showinfo(title="No data file found", message="No data file found.")
    except json.decoder.JSONDecodeError:
        with open("tkinter_pw_manager_passwords.json", "w") as data_file:
            messagebox.showinfo(title="No details for the website exist", message="No details for the website exist")
    else:
        website_found = False
        for website_name in data:
            if string_website == website_name:
                website_found = True
                website_info = data[website_name]
                messagebox.showinfo(title=website_name, message=f'Email: {website_info["email"]}\n'
                                                                f'Password: {website_info["password"]}')
        if not website_found:
            messagebox.showinfo(title="No details for the website exist", message="No details for the website exist")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
img_logo = tkinter.PhotoImage(file="tkinter_pw_manager_logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(column=1, row=0)

label_website = tkinter.Label(text="Website:")
label_website.grid(column=0, row=1)
label_email_username = tkinter.Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)
label_password = tkinter.Label(text="Password:")
label_password.grid(column=0, row=3)

entry_website = tkinter.Entry()
entry_website.grid(column=1, row=1, columnspan=1, sticky="EW")
entry_website.focus()
entry_email_username = tkinter.Entry()
entry_email_username.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_username.insert(0, "fake_email@fakemail.com")
# The "0" above is the index location of where the text will go.
# Alternatively to "0", you can write END, which will put the text at the end of any text that's already there.
entry_password = tkinter.Entry()
entry_password.grid(column=1, row=3, columnspan=1, sticky="EW")

button_search = tkinter.Button(text="Search", command=find_password)
button_search.grid(column=2, row=1, columnspan=1, sticky="EW")
button_generate_password = tkinter.Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3, columnspan=1, sticky="W")
button_add = tkinter.Button(text="Add", command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
