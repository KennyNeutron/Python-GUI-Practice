# This is a Simple Calculator using TKinter
# By: Kenny Neutron (11-14-2024)

import tkinter as tk

print("program start...")
root = tk.Tk()
root.title("Neutron's Simple Calculator")
print("started tkinter...")

string_calculator_screen = tk.StringVar()
str_FirstNumber = tk.StringVar()
str_SecondNumber = tk.StringVar()
this_operation = tk.IntVar()

def Clicked_btn_Equal():
    print("pressed Equal")
    if this_operation.get()==1:
        answer = int(str_FirstNumber.get()) + int(str_SecondNumber.get())
        print("Operation:" + str_FirstNumber.get() + '+' + str_SecondNumber.get())
        string_calculator_screen.set("ans= " + str(answer))

def Clicked_btn_Num1():
    print("pressed #1")
    CheckOperation(1)


def Clicked_btn_Num2():
    print("pressed #2")
    CheckOperation(2)


def Clicked_btn_Add():
    print("pressed Add")
    this_operation.set(1)
    CheckDisplay()

def CheckDisplay():
    print("ThisOperation:" + str(this_operation.get()))
    if this_operation.get() == 0:
        string_calculator_screen.set(str_FirstNumber.get())
    else:
        string_calculator_screen.set(str_FirstNumber.get()+ WhichOperation(this_operation.get()) + str_SecondNumber.get())

def CheckOperation(btn_pressed):
    if this_operation.get() == 0:
        str_FirstNumber.set(str_FirstNumber.get() + str(btn_pressed))
    else:
        str_SecondNumber.set(str_SecondNumber.get() + str(btn_pressed))
    CheckDisplay()

def WhichOperation(Operation):
    if Operation == 1:
        return "+"
    elif Operation == 2:
        return "-"




calculator_screen = tk.Entry(
    root, textvariable=string_calculator_screen, width=60, borderwidth=5
)
calculator_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# ====================================================================
btn_Clr = tk.Button(root, text="CLR", width=12, height=3)
btn_Clr.grid(row=1, column=0)

btn_Divide = tk.Button(root, text="/", width=12, height=3)
btn_Divide.grid(row=1, column=1)

btn_Multiply = tk.Button(root, text="x", width=12, height=3)
btn_Multiply.grid(row=1, column=2)

btn_Subtract = tk.Button(root, text="-", width=12, height=3)
btn_Subtract.grid(row=1, column=3)
# ====================================================================

# ====================================================================
btn_Num7 = tk.Button(root, text="7", width=12, height=3)
btn_Num7.grid(row=2, column=0)

btn_Num8 = tk.Button(root, text="8", width=12, height=3)
btn_Num8.grid(row=2, column=1)

btn_Num9 = tk.Button(root, text="9", width=12, height=3)
btn_Num9.grid(row=2, column=2)

btn_Add = tk.Button(root, text="+", width=12, height=7, command=Clicked_btn_Add)
btn_Add.grid(row=2, column=3, rowspan=2)
# ====================================================================

# ====================================================================
btn_Num4 = tk.Button(root, text="4", width=12, height=3)
btn_Num4.grid(row=3, column=0)

btn_Num5 = tk.Button(root, text="5", width=12, height=3)
btn_Num5.grid(row=3, column=1)

btn_Num6 = tk.Button(root, text="6", width=12, height=3)
btn_Num6.grid(row=3, column=2)
# ====================================================================

# ====================================================================
btn_Num1 = tk.Button(root, text="1", width=12, height=3, command=Clicked_btn_Num1)
btn_Num1.grid(row=4, column=0)

btn_Num2 = tk.Button(root, text="2", width=12, height=3, command=Clicked_btn_Num2)
btn_Num2.grid(row=4, column=1)

btn_Num3 = tk.Button(root, text="3", width=12, height=3)
btn_Num3.grid(row=4, column=2)

btn_Equal = tk.Button(root, text="=", width=12, height=7, command= Clicked_btn_Equal)
btn_Equal.grid(row=4, column=3, rowspan=2)
# ====================================================================

# ====================================================================
btn_Num0 = tk.Button(root, text="0", width=26, height=3)
btn_Num0.grid(row=5, column=0, columnspan=2)

btn_Dot = tk.Button(root, text=".", width=12, height=3)
btn_Dot.grid(row=5, column=2)
# ====================================================================


root.mainloop()
