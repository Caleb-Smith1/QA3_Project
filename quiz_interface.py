import tkinter as tk
from tkinter import messagebox
import sqlite3
from question import Question

def connect_db():
    return sqlite3.connect("quiz.db")

def fetch_questions(course_table):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM {course_table} LIMIT 2")
    rows = cursor.fetchall()
    conn.close()

    questions = []
    for row in rows:
        question_text = row[0]
        options = [opt for opt in row[1:5] if opt is not None]
        correct_answer = row[5]
        questions.append(Question(question_text, options, correct_answer))
    return questions

def show_quiz_menu():
    menu_window = tk.Tk()
    menu_window.title("Choose a Quiz Category")
    menu_window.geometry("300x300")

    tk.Label(menu_window, text="Select a Quiz Category", font=("Helvetica", 14)).pack(pady=20)

    categories = {
        "Database Administration": "database_admin",
        "Microeconomics": "microeconomics",
        "Business Management": "business_mgmt",
        "Business Statistics": "statistics",
        "App Development": "app_dev"
    }

    def start_quiz(category_table):
        menu_window.destroy()
        show_quiz(category_table)

    for name, table in categories.items():
        tk.Button(menu_window, text=name, width=30, command=lambda t=table: start_quiz(t)).pack(pady=5)

    menu_window.mainloop()

# Placeholder to be replaced next step
def show_quiz(course_table):
    messagebox.showinfo("Quiz Start", f"Loading quiz for: {course_table}")
