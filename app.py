import tkinter as tk

def display_string():
    entry_var.set("Hello, Tkinter!")  # Set the string to display in the Entry

root = tk.Tk()
root.title("Display String in Entry")

# Create a StringVar to hold the text
entry_var = tk.StringVar()

# Create an Entry widget with the StringVar
entry = tk.Entry(root, textvariable=entry_var, width=30)
entry.pack(pady=10)

# Create a Button to trigger the string display
button = tk.Button(root, text="Display Text", command=display_string)
button.pack(pady=5)

root.mainloop()