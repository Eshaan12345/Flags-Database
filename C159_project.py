# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:35:54 2024

@author: Eshaan Gurjar
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x700")

flag = ""

Jp = ImageTk.PhotoImage(Image.open("Jp.jpg"))
Id = ImageTk.PhotoImage(Image.open("Id.png"))
UA = ImageTk.PhotoImage(Image.open("Ua.png"))

dict1 = {
            "Japan" : Jp,
            "India" : Id,
            "USA" : UA
        }

text = Entry(root)
text.place(relx = 0.5, rely = 0.2, anchor = CENTER)

image = Label(root)
image.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def search():
    global flag
    try:
        flag = text.get()
        image["image"] = dict1[flag]
        print(flag)
     
    except KeyError:
        messagebox.showinfo("Error", "Flag not in database")
     

button = Button(root, text = "Search", command = search)
button.place(relx = 0.5, rely = 0.3, anchor = CENTER)

root.mainloop()