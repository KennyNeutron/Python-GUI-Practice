# This is TKinter Training
# November 8, 2024

from tkinter import *

print("program start...")
root = Tk()
print("started tkinter...")


entry_name = Entry(root, width=50, borderwidth=5)
entry_name.grid(row=0, column=0)


def myButton_Clicked():
    text_to_display=""
    if entry_name.get() == "" :
        text_to_display = "Name Cannot be empty!"
    else:
        text_to_display = "Hello " + entry_name.get() + " Welcome!"
    myLabel = Label(root, text=text_to_display)
    myLabel.grid(row=2, column=0)


myButton = Button(root, text="Click Me", command=myButton_Clicked)
myButton.grid(row=1, column=0, sticky="w")


root.mainloop()
