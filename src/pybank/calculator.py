import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Calculator")
root.geometry("320x350")
root.resizable(False, False)

def add():
    pass

def subract():
    pass

def multiply():
    pass

def divide():
    pass

def clear():
    display.delete(0, ctk.END)
    
display = ctk.CTkEntry(
    root,
    width=280,
    height=55,
    font=("Arial", 24),
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=(15, 10))

buttons = [
    ("C", 1, 0), ("÷", 1, 1), ("×", 1, 2), ("−", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("=", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("0", 4, 3),
]

for text, row, column in buttons:
    button = ctk.CTkButton(
        root,
        text=text,
        width=60,
        height=55,
        font=("Arial", 18)
    )
    button.grid(row=row, column=column, padx=4, pady=4)

root.mainloop()