# QA3_Project
## Quiz Bowl Application

This is a graphical Quiz Bowl application created in Python using Tkinter and SQLite. It allows students to take quizzes based on five course categories and gives administrators full control to manage the questions.

## How to run the app

1. Make sure Python 3 is installed on your computer.
2. Download or clone the repository.
3. In the project folder, open a terminal or command prompt.
4. Run the windows.py file

# Admin Access
Click the Admin button on the main screen. You’ll be asked to enter the admin password.

# Admin Password
    admin123

Once logged in, you can:
View all questions and answers,
Add new questions,
Edit existing questions,
Delete questions by exact text,

# Taking a quiz
1. Click Take Quiz from the main menu.
2. Select a course category from the list.
3. The quiz will start, showing all available questions (randomized order).
4. Select your answer from a dropdown and click Submit.
5. You'll receive immediate feedback after each question.
6. A final score will be displayed at the end of the quiz.

# Project Files

1. **window.py** – Launches the app with Admin and Student options.
2. **admin_panel.py** – Admin panel to view, add, edit, and delete questions.
3. **quiz_interface.py** – Student quiz screen with answer feedback and scoring.
4. **question.py** – Defines the Question class and checks if answers are correct.
5. **database.py** – Creates the database and course tables.
6. **quiz.db** – Stores all quiz questions and answers.
7. **remove_duplicates.py** – Removes duplicate questions from the database.
8. **check_questions.py** – Lists all current questions in the terminal.
9. **README.md** – This file. Explains how to run and use the app.
