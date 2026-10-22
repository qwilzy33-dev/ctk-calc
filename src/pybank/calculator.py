
import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Calculator")
root.geometry("320x260")
root.resizable(False, False)

first_number = None
operator = None
new_number = True
expression = ""


def add():
    calculate("+")


def subtract():
    calculate("-")


def multiply():
    calculate("*")


def divide():
    calculate("/")


def calculate(op):
    global first_number, operator, new_number, expression

    try:
        if operator is not None and not new_number:
            second_number = float(display.get())

            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "*":
                result = first_number * second_number
            elif operator == "/":
                if second_number == 0:
                    display.delete(0, ctk.END)
                    display.insert(0, "Error")
                    first_number = None
                    operator = None
                    new_number = True
                    expression = ""
                    return

                result = first_number / second_number

            first_number = result

        else:
            first_number = float(display.get())

        operator = op
        expression = f"{first_number}{op}"
        display.delete(0, ctk.END)
        display.insert(0, expression)
        new_number = True

    except ValueError:
        display.delete(0, ctk.END)
        display.insert(0, "Error")
        first_number = None
        operator = None
        new_number = True
        expression = ""


def equals():
    global first_number, operator, new_number, expression

    if operator is not None and not new_number:
        calculate(operator)
        operator = None
        new_number = True
        expression = ""


def clear():
    global first_number, operator, new_number, expression

    display.delete(0, ctk.END)
    first_number = None
    operator = None
    new_number = True
    expression = ""


def press_number(number):
    global new_number

    if new_number or display.get() == "Error":
        display.delete(0, ctk.END)
        new_number = False

    display.insert(ctk.END, number)


display = ctk.CTkEntry(
    root,
    width=280,
    height=45,
    font=("Arial", 24),
    justify="right"
)
display.grid(
    row=0, column=0, columnspan=4,
    padx=10, pady=(8, 4)
)

buttons = [
    ("C", 1, 0), ("÷", 1, 1), ("×", 1, 2), ("−", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("0", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
]

for text, row, column in buttons:
    if text == "C":
        command = clear
    elif text == "+":
        command = add
    elif text == "−":
        command = subtract
    elif text == "×":
        command = multiply
    elif text == "÷":
        command = divide
    elif text == "=":
        command = equals
    else:
        command = lambda value=text: press_number(value)

    button = ctk.CTkButton(
        root,
        text=text,
        width=60,
        height=40,
        font=("Arial", 18),
        command=command
    )
    button.grid(row=row, column=column, padx=4, pady=2)

root.mainloop()
