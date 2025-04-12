import tkinter as tk
from tkinter import messagebox
import admin_panel  # will build next
import quiz_interface  # will build after that

ADMIN_PASSWORD = "admin123"  # This will go in the README

def open_admin_login():
    def check_password():
        if password_entry.get() == ADMIN_PASSWORD:
            login_window.destroy()
            admin_panel.show_admin_panel()
        else:
            messagebox.showerror("Error", "Incorrect password")

    login_window = tk.Toplevel(root)
    login_window.title("Admin Login")
    login_window.geometry("300x150")

    tk.Label(login_window, text="Enter Admin Password:").pack(pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()
    tk.Button(login_window, text="Submit", command=check_password).pack(pady=10)

def open_quiz_menu():
    root.destroy()
    quiz_interface.show_quiz_menu()

root = tk.Tk()
root.title("Quiz Bowl")
root.geometry("300x200")

tk.Label(root, text="Welcome to Quiz Bowl!", font=("Helvetica", 14)).pack(pady=20)
tk.Button(root, text="Admin", width=20, command=open_admin_login).pack(pady=10)
tk.Button(root, text="Take Quiz", width=20, command=open_quiz_menu).pack(pady=10)

root.mainloop()
