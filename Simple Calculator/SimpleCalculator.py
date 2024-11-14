# This is a Simple Calculator using TKinter
# By: Kenny Neutron (11-14-2024)

import tkinter as tk
from tkinter import font
from tkinter import PhotoImage

print("program start...")
root = tk.Tk()
root.title("Neutron's Simple Calculator")
# Configure grid row and column sizes
root.rowconfigure(1, minsize=5)  # Fix row height for the button
root.columnconfigure(0, minsize=5)  # Fix column width for consistency

print("started tkinter...")

icon = PhotoImage(file="Simple Calculator/calculator.png")
root.iconphoto(False, icon)

button_font = font.Font(family="Helvetica", size=8, weight="bold")
label_font = font.Font(family="Helvetica", size=10, weight="bold")

string_calculator_screen = tk.StringVar()
str_FirstNumber = tk.StringVar()
str_SecondNumber = tk.StringVar()
this_operation = tk.IntVar()
has_decimal = tk.BooleanVar()
FN_has_decimal=tk.BooleanVar()
SN_has_decimal=tk.BooleanVar()

def Clicked_btn_Dot():
    if not has_decimal.get():
        if not this_operation.get():
            if len(str_FirstNumber.get()) > 0:
                str_FirstNumber.set(str_FirstNumber.get()+".")
                has_decimal.set(True)
                FN_has_decimal.set(True)
                CheckDisplay()
        else:
            if len(str_SecondNumber.get()) > 0:
                str_SecondNumber.set(str_SecondNumber.get()+".")
                has_decimal.set(True)
                SN_has_decimal.set(True)
                CheckDisplay()
    else:
        if not this_operation.get():
            print("First Number has Decimal already")
        else:
            print("Second Number has Decimal already")

def Clicked_btn_Clear():
    print("pressed Clear")
    string_calculator_screen.set("")
    str_FirstNumber.set("")
    str_SecondNumber.set("")
    this_operation.set(0)
    has_decimal.set(False)
    FN_has_decimal.set(False)
    SN_has_decimal.set(False)

def Clicked_btn_Equal():
    print("pressed Equal")
    answer=0
    if not this_operation.get():
        print("cannot answer, no operation declared!")
    else:
        if not str_SecondNumber.get():
            print("cannot answer, no second number")
        else:
            if FN_has_decimal.get() and not SN_has_decimal.get():
                if this_operation.get()==1:
                    answer = float(str_FirstNumber.get()) + int(str_SecondNumber.get())
                elif this_operation.get()==2:
                    answer = float(str_FirstNumber.get()) - int(str_SecondNumber.get())
                elif this_operation.get()==3:
                    answer = float(str_FirstNumber.get()) * int(str_SecondNumber.get())
                elif this_operation.get()==4:
                    answer = float(str_FirstNumber.get()) / int(str_SecondNumber.get())
            elif not FN_has_decimal.get() and  SN_has_decimal.get():
                if this_operation.get()==1:
                    answer = int(str_FirstNumber.get()) + float(str_SecondNumber.get())
                elif this_operation.get()==2:
                    answer = int(str_FirstNumber.get()) - float(str_SecondNumber.get())
                elif this_operation.get()==3:
                    answer = int(str_FirstNumber.get()) * float(str_SecondNumber.get())
                elif this_operation.get()==4:
                    answer = int(str_FirstNumber.get()) / float(str_SecondNumber.get())
            else:
                if this_operation.get()==1:
                    answer = int(str_FirstNumber.get()) + int(str_SecondNumber.get())
                elif this_operation.get()==2:
                    answer = int(str_FirstNumber.get()) - int(str_SecondNumber.get())
                elif this_operation.get()==3:
                    answer = int(str_FirstNumber.get()) * int(str_SecondNumber.get())
                elif this_operation.get()==4:
                    answer = int(str_FirstNumber.get()) / int(str_SecondNumber.get())
            string_calculator_screen.set("ans= " + str(answer))
            print("Operation:" + str_FirstNumber.get() + WhichOperation(this_operation.get()) + str_SecondNumber.get() + "=" +str(answer))


def Clicked_btn_Num1():
    print("pressed #1")
    CheckOperation(1)

def Clicked_btn_Num2():
    print("pressed #2")
    CheckOperation(2)

def Clicked_btn_Num3():
    print("pressed #3")
    CheckOperation(3)

def Clicked_btn_Num4():
    print("pressed #4")
    CheckOperation(4)

def Clicked_btn_Num5():
    print("pressed #5")
    CheckOperation(5)

def Clicked_btn_Num6():
    print("pressed #6")
    CheckOperation(6)

def Clicked_btn_Num7():
    print("pressed #7")
    CheckOperation(7)

def Clicked_btn_Num8():
    print("pressed #8")
    CheckOperation(8)

def Clicked_btn_Num9():
    print("pressed #9")
    CheckOperation(9)

def Clicked_btn_Num0():
    print("pressed #0")
    if this_operation.get()==0:
        if not str_FirstNumber.get():
            print("first number can't strat from 0")
        else:
            CheckOperation(0)
    else:
        if not str_SecondNumber.get():
            print("second number can't strat from 0")
        else:
            CheckOperation(0)

def Clicked_btn_Add():
    print("pressed Add")
    this_operation.set(1)
    has_decimal.set(False)
    CheckDisplay()

def Clicked_btn_Subtract():
    print("pressed Subtract")
    this_operation.set(2)
    has_decimal.set(False)
    CheckDisplay()

def Clicked_btn_Multiply():
    print("pressed Multiply")
    this_operation.set(3)
    has_decimal.set(False)
    CheckDisplay()

def Clicked_btn_Divide():
    print("pressed Divide")
    this_operation.set(4)
    has_decimal.set(False)
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
    elif Operation == 3:
        return "x"
    elif Operation == 4:
        return "/"




calculator_screen = tk.Entry(
    root, textvariable=string_calculator_screen, width=60, borderwidth=5,font=label_font
)
calculator_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# ====================================================================
btn_Clr = tk.Button(root, text="CLR", width=12, height=3, font=button_font, padx=0.1, pady=0.1,command=Clicked_btn_Clear)
btn_Clr.grid(row=1, column=0)

btn_Divide = tk.Button(root, text="/", width=12, height=3, font=button_font, command=Clicked_btn_Divide)
btn_Divide.grid(row=1, column=1)

btn_Multiply = tk.Button(root, text="x", width=12, height=3, font=button_font, command=Clicked_btn_Multiply)
btn_Multiply.grid(row=1, column=2)

btn_Subtract = tk.Button(root, text="-", width=12, height=3, font=button_font, command=Clicked_btn_Subtract)
btn_Subtract.grid(row=1, column=3)
# ====================================================================

# ====================================================================
btn_Num7 = tk.Button(root, text="7", width=12, height=3, font=button_font, command=Clicked_btn_Num7)
btn_Num7.grid(row=2, column=0)

btn_Num8 = tk.Button(root, text="8", width=12, height=3, font=button_font, command=Clicked_btn_Num8)
btn_Num8.grid(row=2, column=1)

btn_Num9 = tk.Button(root, text="9", width=12, height=3, font=button_font, command=Clicked_btn_Num9)
btn_Num9.grid(row=2, column=2)

btn_Add = tk.Button(root, text="+", width=12, height=7, font=button_font, command=Clicked_btn_Add)
btn_Add.grid(row=2, column=3, rowspan=2)
# ====================================================================

# ====================================================================
btn_Num4 = tk.Button(root, text="4", width=12, height=3, font=button_font, command=Clicked_btn_Num4)
btn_Num4.grid(row=3, column=0)

btn_Num5 = tk.Button(root, text="5", width=12, height=3, font=button_font, command=Clicked_btn_Num5)
btn_Num5.grid(row=3, column=1)

btn_Num6 = tk.Button(root, text="6", width=12, height=3, font=button_font, command=Clicked_btn_Num6)
btn_Num6.grid(row=3, column=2)
# ====================================================================

# ====================================================================
btn_Num1 = tk.Button(root, text="1", width=12, height=3, font=button_font, command=Clicked_btn_Num1)
btn_Num1.grid(row=4, column=0)

btn_Num2 = tk.Button(root, text="2", width=12, height=3, font=button_font, command=Clicked_btn_Num2)
btn_Num2.grid(row=4, column=1)

btn_Num3 = tk.Button(root, text="3", width=12, height=3, font=button_font, command=Clicked_btn_Num3)
btn_Num3.grid(row=4, column=2)

btn_Equal = tk.Button(root, text="=", width=12, height=7, font=button_font, command= Clicked_btn_Equal)
btn_Equal.grid(row=4, column=3, rowspan=2)
# ====================================================================

# ====================================================================
btn_Num0 = tk.Button(root, text="0", width=28, height=3, font=button_font, command=Clicked_btn_Num0)
btn_Num0.grid(row=5, column=0, columnspan=2)

btn_Dot = tk.Button(root, text=".", width=12, height=3, font=button_font, command=Clicked_btn_Dot)
btn_Dot.grid(row=5, column=2)
# ====================================================================


root.mainloop()
