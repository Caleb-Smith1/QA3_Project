import tkinter as tk
import sqlite3

def connect_db():
    return sqlite3.connect("quiz.db")

def fetch_all_questions():
    conn = connect_db()
    cursor = conn.cursor()

    tables = {
        "database_admin": "Database Administration",
        "microeconomics": "Microeconomics",
        "business_mgmt": "Business Management",
        "statistics": "Business Statistics",
        "app_dev": "Business App Development"
    }

    all_questions = []

    for table, label in tables.items():
        cursor.execute(f"SELECT question, correct_answer FROM {table}")
        rows = cursor.fetchall()
        for question, answer in rows:
            all_questions.append((label, question, answer))

    conn.close()
    return all_questions

def show_admin_panel():
    admin_window = tk.Tk()
    admin_window.title("Admin Panel")
    admin_window.geometry("600x400")

    tk.Label(admin_window, text="All Questions and Answers", font=("Helvetica", 14)).pack(pady=10)

    questions = fetch_all_questions()

    text_area = tk.Text(admin_window, wrap=tk.WORD, width=70, height=20)
    text_area.pack(padx=10, pady=10)

    for category, question, answer in questions:
        text_area.insert(tk.END, f"[{category}]\nQ: {question}\nA: {answer}\n\n")

    text_area.config(state=tk.DISABLED)

    admin_window.mainloop()
