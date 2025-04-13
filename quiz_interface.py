import tkinter as tk
from tkinter import messagebox
import sqlite3
from question import Question

def connect_db():
    return sqlite3.connect("quiz.db")

def fetch_questions(course_table):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT question, option_a, option_b, option_c, option_d, correct_answer
        FROM {course_table}
        LIMIT 10
    """)
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

def show_quiz(course_table):
    questions = fetch_questions(course_table)

    if not questions:
        messagebox.showerror("Error", f"No questions found for {course_table}")
        return

    score = [0]
    index = [0]

    quiz_window = tk.Tk()
    quiz_window.title("Quiz Time")
    quiz_window.geometry("500x300")

    question_label = tk.Label(quiz_window, text="", wraplength=400, font=("Helvetica", 12))
    question_label.pack(pady=20)

    selected_option = tk.StringVar(quiz_window)
    selected_option.set("Select one")
    option_menu = tk.OptionMenu(quiz_window, selected_option, "Select one")
    option_menu.pack()

    feedback_label = tk.Label(quiz_window, text="", font=("Helvetica", 10))
    feedback_label.pack(pady=10)

    def load_question():
        q = questions[index[0]]
        question_label.config(text=f"Q{index[0]+1}: {q.question_text}")

        selected_option.set("Select one")

        menu = option_menu["menu"]
        menu.delete(0, "end")
        menu.add_command(label="Select one", command=tk._setit(selected_option, "Select one"))
        for opt in q.options:
            menu.add_command(label=opt, command=tk._setit(selected_option, opt))

    def submit_answer():
        q = questions[index[0]]
        answer = selected_option.get()

        if answer == "Select one":
            messagebox.showwarning("Wait", "Please select an answer before submitting.")
            return

        if q.is_correct(answer):
            feedback_label.config(text="✅ Correct!", fg="green")
            score[0] += 1
        else:
            feedback_label.config(text=f"❌ Incorrect! Correct answer: {q.correct_answer}", fg="red")

        index[0] += 1
        if index[0] < len(questions):
            quiz_window.after(1000, load_question)
        else:
            quiz_window.after(1500, lambda: show_score(score[0], len(questions)))

    def show_score(correct, total):
        quiz_window.destroy()
        result_window = tk.Tk()
        result_window.title("Quiz Result")
        result_window.geometry("300x150")
        tk.Label(result_window, text=f"You scored {correct} out of {total}!", font=("Helvetica", 14)).pack(pady=30)
        tk.Button(result_window, text="Close", command=result_window.destroy).pack()

    tk.Button(quiz_window, text="Submit Answer", command=submit_answer).pack(pady=20)

    load_question()
    quiz_window.mainloop()
