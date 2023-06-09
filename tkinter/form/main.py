from tkinter import *
from lib import window_geometry

def update_data():
    data["first_name"] = first_name_entry.get()
    data["last_name"] = last_name_entry.get()
    data["email"] = email_entry.get()
    data["password"] = password_entry.get()
    print(data)

data = {}

root = Tk()
root.title="Registration Form"
root.geometry(window_geometry(root))


# body
body = Frame(root)
body.pack(fill="both", expand=True, padx=20, pady=20)


# welcome
welcome = Label(body, text="Welcome to the registration form")
welcome.pack(fill="both", side="top", expand=True)

# first_name
first_name = Frame(body)
first_name.pack(fill="x", side="top")

firt_name_label = Label(first_name, text="First Name", width=15, anchor="w")
firt_name_label.pack(fill="x", side="left")
first_name_entry = Entry(first_name)
first_name_entry.pack(fill="x", side="right", expand=True)


# last_name
last_name = Frame(body)
last_name.pack(fill="x", side="top")

last_name_label = Label(last_name, text="Last Name", width=15, anchor="w")
last_name_label.pack(fill="x", side="left")
last_name_entry = Entry(last_name)
last_name_entry.pack(fill="x", side="right", expand=True)


# email
email = Frame(body)
email.pack(fill="x", side="top")

email_label = Label(email, text="Email", width=15, anchor="w")
email_label.pack(fill="x", side="left")
email_entry = Entry(email)
email_entry.pack(fill="x", side="right", expand=True)


# password
password = Frame(body)
password.pack(fill="x", side="top")

password_label = Label(password, text="Password", width=15, anchor="w")
password_label.pack(fill="x", side="left")
password_entry = Entry(password)
password_entry.pack(fill="x", side="right", expand=True)


result = Button(body, text="Submit", command=lambda:update_data())
result.pack(fill="x", side="top")


root.mainloop()