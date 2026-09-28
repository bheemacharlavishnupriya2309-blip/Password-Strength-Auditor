import tkinter as tk
from tkinter import messagebox

from password_checker import PasswordChecker
from password_generator import PasswordGenerator
from security_report import SecurityReport


def audit_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    checker = PasswordChecker()
    result = checker.check_password(password)

    report = SecurityReport().generate(result)

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, report)


def generate_password():
    try:
        length = int(length_entry.get())

        generator = PasswordGenerator()
        password = generator.generate(length=length)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        audit_password()

    except ValueError as error:
        messagebox.showerror("Error", str(error))


root = tk.Tk()
root.title("Password Strength Auditor & Policy Checker")
root.geometry("650x600")
root.resizable(False, False)

title = tk.Label(
    root,
    text="PASSWORD STRENGTH AUDITOR",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

password_label = tk.Label(
    root,
    text="Enter Password",
    font=("Arial", 12)
)
password_label.pack()

password_entry = tk.Entry(
    root,
    width=45,
    font=("Arial", 12),
    show="*"
)
password_entry.pack(pady=10)

audit_button = tk.Button(
    root,
    text="Audit Password",
    command=audit_password,
    width=20
)
audit_button.pack(pady=5)

length_label = tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12)
)
length_label.pack(pady=(20, 5))

length_entry = tk.Entry(
    root,
    width=10,
    font=("Arial", 12)
)
length_entry.insert(0, "16")
length_entry.pack()

generate_button = tk.Button(
    root,
    text="Generate Secure Password",
    command=generate_password,
    width=25
)
generate_button.pack(pady=10)

result_text = tk.Text(
    root,
    width=70,
    height=20,
    font=("Consolas", 10)
)
result_text.pack(pady=15)

root.mainloop()