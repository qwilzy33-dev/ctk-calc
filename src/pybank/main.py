import customtkinter as ctk

ctk.set_appearance_mode("dark")

root =  ctk.CTk()
root.title("PyBank")
root.geometry("600x400")

title = ctk.CTkLabel(
    root,
    text="Welcome to PyBank",
    font=("Arial", 24)
)
title.pack(pady=30)

create_account_button = ctk.CTkButton(
    root,
    text="Create Account a new Account"
)
create_account_button.pack(pady=10)

login_button = ctk.CTkButton(
    root,
    text="Log In to an Account"
)
login_button.pack(pady=10)

root.mainloop()