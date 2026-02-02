import random
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    numbers = [0,1,2,3,4,5,6,7,8,9]
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    special = ["!","@","#","$","%","^","&","*"]
    final = numbers + letters + special
    password = ""

    for _ in range(10):
        password += str(random.choice(final))
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    user_website = website_entry.get()
    user_mail = mail_entry.get()
    user_password = password_entry.get()

    if len(user_password) == 0 or len(user_website) == 0 or len(user_mail) == 0:
        messagebox.showerror("Error", "Please enter all required information")

    else:
        ask = messagebox.askokcancel(f"{user_website}",
                                     f"The details you entered:\nWebsite: {user_website}\nEmail/ Username: {user_mail}\nPassword: {user_password}\n"
                                     f"Want to save and continue?")
        if ask:
            with open('user_data.txt', 'a') as file:
                file.write(f"{user_website} | {user_mail} | {user_password}\n")

            website_entry.delete(0, END)
            mail_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(500, 400)
window.config(padx = 30, pady =30)

# CANVAS
canvas = Canvas(width=200, height=189)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,98,image=logo)
canvas.grid(row= 2, column=3)

# WEBSITE NAME
website_text = Label(text= "Website:", font=("Sans Serif", 10))
website_text.grid(row=3, column=2)
website_entry = Entry(width=30)    #or set width to 35
website_entry.focus()
website_entry.grid(row= 3, column=3, columnspan=2, sticky=W+E)

# MAIL/ USERID
mail_text = Label(text= "Email / Username:", font=("Sans Serif", 10))
mail_text.grid(row=4, column=2)
mail_entry = Entry(width=30)   #or set width to 35
mail_entry.grid(row= 4, column=3, columnspan=2, sticky=W+E)

# ENTER PASSWORD
password_text = Label(text= "Password:", font=("Sans Serif", 10))
password_text.grid(row=5, column=2)
password_entry = Entry(width=33)
password_entry.grid(row= 5, column=3, sticky=W)

# GENERATE A RANDOM PASSWORD
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=5, column=4)

# SAVE ALL THIS TO A NOTE
add_password = Button(text="Add", command=save_password)   #or set width to 36
add_password.grid(row=6, column=3, columnspan=4, sticky=W+E)

window.mainloop()