#Building a calculator in python

import tkinter as tk

def button_press(num):
    pass

def equals():
    pass

def clear():
    pass

window = tk.Tk()
window.title("Basic Calculator Program")
window.geometry("500x500")

equation_text = ""

equation_label = tk.StringVar()

label = tk.Label(window, textvariable=equation_label,
                font=("Times New Roman", 20))

window.mainloop()



def main():
    operator = input("Enter an operator(+ - * /): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+": #We are inputing the plus operator as a string variable
        result = num1 + num2
# we won't be using operator() because it's a string
#not a function

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
       result = num1 / num2

    else:
        print(f"{operator} is not a valid operator. Please input +, -, *, or /")
        return

    print ("Result:", result)

if __name__ = "__main__":
    main()
