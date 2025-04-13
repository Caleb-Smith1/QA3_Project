import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

tables = ["database_admin", "microeconomics", "business_mgmt", "statistics", "app_dev"]

for table in tables:
    cursor.execute(f"SELECT question, correct_answer FROM {table}")
    rows = cursor.fetchall()
    print(f"\n{table} ({len(rows)} questions):")
    for q, a in rows:
        print(f"  Q: {q} → A: {a}")

conn.close()
