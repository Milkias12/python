# importing the tkinter module
from tkinter import *
import tkinter.messagebox as messagebox

import random

root = Tk()
root.geometry("400x400")    # x is small case here

passstr = StringVar()
passlen = IntVar()

passlen.set("")


def generate():
    # storing the keys in a list which will be used to generate
    # the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']

    # declaring the empty string
    password = ""

    # loop to generate the random password of the length entered
    # by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard


def copytoclipboard():
    random_password = passstr.get()
    root.clipboard_clear()
    root.clipboard_append(random_password)
    messagebox.showinfo("Password Copied", "Password copied to clipboard")


Label(root, text="Password Generator Application", font="calibri 20 bold").pack()

Label(root, text="Enter password length").pack(pady=3)

Entry(root, textvariable=passlen).pack(pady=3)

# button to call the generate function
Button(root, text="Generate Password", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(root, textvariable=passstr).pack(pady=3)

# button to call the copytoclipboard function
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()
root.mainloop()
