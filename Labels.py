# This is TKinter Training
# November 8, 2024

from tkinter import *

print("program start...")
root = Tk()
print("started tkinter...")


myLabel = Label(root, text="This is a text from row0 and column0")
myLabel.grid(row=0, column=0)

myLabel2 = Label(root, text="This is a text from row1 and column1")
myLabel2.grid(row=1,column=1)

myLabel3 = Label(root, text="This is a text from row2 and column0")
myLabel3.grid(row=2,column=0)

myLabel4 = Label(root, text= "This is a text from row2 and column2")
myLabel4.grid(row=2, column=2)

#myLabel.pack()

root.mainloop()