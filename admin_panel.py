import tkinter as tk
from tkinter import messagebox
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

def add_question_form(parent_window):
    form = tk.Toplevel(parent_window)
    form.title("Add New Question")
    form.geometry("500x500")

    tk.Label(form, text="Course:").pack()
    course_var = tk.StringVar(form)
    course_var.set("database_admin")
    tk.OptionMenu(form, course_var, "database_admin", "microeconomics", "business_mgmt", "statistics", "app_dev").pack()

    fields = {}
    for label in ["Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer"]:
        tk.Label(form, text=label).pack()
        entry = tk.Entry(form, width=60)
        entry.pack()
        fields[label] = entry

    def submit():
        values = [fields[field].get().strip() for field in fields]
        if not all(values) or course_var.get() == "":
            messagebox.showwarning("Incomplete", "Please fill out all fields.")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO {course_var.get()} (question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, values)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Question added!")
        form.destroy()

    tk.Button(form, text="Submit", command=submit).pack(pady=10)

def delete_question_form(parent_window):
    form = tk.Toplevel(parent_window)
    form.title("Delete a Question")
    form.geometry("500x250")

    # Label for course selection
    tk.Label(form, text="Select Course:").pack()

    # Define dropdown options and default value
    course_var = tk.StringVar(form)
    course_options = ["database_admin", "microeconomics", "business_mgmt", "statistics", "app_dev"]
    course_var.set(course_options[0])  # set default

    # Create dropdown
    course_menu = tk.OptionMenu(form, course_var, *course_options)
    course_menu.pack()

    # Question entry
    tk.Label(form, text="Enter Exact Question Text to Delete:").pack()
    question_entry = tk.Entry(form, width=60)
    question_entry.pack(pady=5)

    def delete_question():
        question_text = question_entry.get().strip()
        if not question_text:
            messagebox.showwarning("Missing Info", "Please enter the question text.")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {course_var.get()} WHERE question = ?", (question_text,))
        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        if deleted > 0:
            messagebox.showinfo("Success", f"Deleted {deleted} question(s).")
        else:
            messagebox.showwarning("Not Found", "No matching question found.")
        form.destroy()

    # Delete button
    tk.Button(form, text="Delete", command=delete_question).pack(pady=10)



def show_admin_panel():
    admin_window = tk.Tk()
    admin_window.title("Admin Panel")
    admin_window.geometry("600x500")

    tk.Label(admin_window, text="All Questions and Answers", font=("Helvetica", 14)).pack(pady=10)

    questions = fetch_all_questions()

    text_area = tk.Text(admin_window, wrap=tk.WORD, width=70, height=20)
    text_area.pack(padx=10, pady=10)

    for category, question, answer in questions:
        text_area.insert(tk.END, f"[{category}]\nQ: {question}\nA: {answer}\n\n")

    text_area.config(state=tk.DISABLED)

    # Admin action buttons
    tk.Button(admin_window, text="Add New Question", command=lambda: add_question_form(admin_window)).pack(pady=5)
    tk.Button(admin_window, text="Delete Question", command=lambda: delete_question_form(admin_window)).pack(pady=5)
    tk.Button(admin_window, text="Edit Question", command=lambda: edit_question_form(admin_window)).pack(pady=5)

    admin_window.mainloop()
def edit_question_form(parent_window):
    form = tk.Toplevel(parent_window)
    form.title("Edit a Question")
    form.geometry("500x600")

    tk.Label(form, text="Select Course:").pack()
    course_var = tk.StringVar()
    course_var.set("database_admin")
    tk.OptionMenu(form, course_var, "database_admin", "microeconomics", "business_mgmt", "statistics", "app_dev").pack()

    tk.Label(form, text="Enter EXACT question text to edit:").pack()
    old_question_entry = tk.Entry(form, width=60)
    old_question_entry.pack()

    tk.Label(form, text="New Question Text:").pack()
    new_question_entry = tk.Entry(form, width=60)
    new_question_entry.pack()

    fields = {}
    for label in ["Option A", "Option B", "Option C", "Option D", "Correct Answer"]:
        tk.Label(form, text=label).pack()
        entry = tk.Entry(form, width=60)
        entry.pack()
        fields[label] = entry

    def submit():
        old_text = old_question_entry.get().strip()
        new_text = new_question_entry.get().strip()
        option_a = fields["Option A"].get().strip()
        option_b = fields["Option B"].get().strip()
        option_c = fields["Option C"].get().strip()
        option_d = fields["Option D"].get().strip()
        correct_answer = fields["Correct Answer"].get().strip()

        if not old_text or not new_text or not option_a or not option_b or not correct_answer:
            messagebox.showwarning("Incomplete", "Please fill out at least Option A, Option B, and Correct Answer.")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE {course_var.get()}
            SET question = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, correct_answer = ?
            WHERE question = ?
        """, (
            new_text,
            option_a,
            option_b,
            option_c if option_c else None,
            option_d if option_d else None,
            correct_answer,
            old_text
        ))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Question updated!")
        form.destroy()

    tk.Button(form, text="Save Changes", command=submit).pack(pady=10)
