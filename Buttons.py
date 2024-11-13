# This is TKinter Training
# November 8, 2024

from tkinter import *

print("program start...")
root = Tk()
print("started tkinter...")

def myButton_Clicked():
    myLabel= Label(root, text="Button Clicked")
    myLabel.grid(row=1, column=0)

myButton = Button(root, text="Click Me", command=myButton_Clicked)
myButton.grid(row=0,column=0)



root.mainloop()