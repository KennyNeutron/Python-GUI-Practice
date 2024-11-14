import tkinter as tk
from tkinter import PhotoImage

print("program start...")
root = tk.Tk()
root.title("Images Practice")
print("started tkinter...")


icon = PhotoImage(file="picture.png")
root.iconphoto(False, icon)

root.mainloop()