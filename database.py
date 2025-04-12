import sqlite3

def connect_db():
    return sqlite3.connect("quiz.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    tables = {
        "database_admin": "Database Administration",
        "microeconomics": "Microeconomics",
        "business_mgmt": "Business Management",
        "statistics": "Business Statistics",
        "app_dev": "Business App Development"
    }

    for table in tables:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                option_a TEXT,
                option_b TEXT,
                option_c TEXT,
                option_d TEXT,
                correct_answer TEXT NOT NULL
            );
        """)

    conn.commit()
    conn.close()

def insert_sample_questions():
    conn = connect_db()
    cursor = conn.cursor()

    questions = [
        # Database Admin
        ("database_admin", "True or False: Primary keys must be unique.", "True", "False", None, None, "True"),
        ("database_admin", "True or False: NOSQL means 'not only sql'", "True", "False", None, None, "True"),

        # Microeconomics
        ("microeconomics", "What is the definition of scarcity?", "Unlimited wants, limited resources", "Only prices rising", "Consumers buying more", "Producers selling less", "Unlimited wants, limited resources"),
        ("microeconomics", "True or False: Causation always implies correlation.", "True", "False", None, None, "False"),

        # Business Management
        ("business_mgmt", "Which is NOT a component of attitude?", "Behavioral", "Cognitive", "Physical", "Affective", "Physical"),
        ("business_mgmt", "True or False: Ethics in business are always covered by the legal system.", "True", "False", None, None, "False"),

        # Statistics
        ("statistics", "What is the most frequently occurring value called?", "Mean", "Mode", "Median", "Range", "Mode"),
        ("statistics", "True or False: Range is a good measure of dispersion.", "True", "False", None, None, "False"),

        # App Dev
        ("app_dev", "What is the output of print('5+5')?", "10", "55", "5+5", "Error", "5+5"),
        ("app_dev", "What is the output of print(8*10)?", "810", "80", "8*10", "Error", "80")
    ]

    for q in questions:
        cursor.execute(f"""
            INSERT INTO {q[0]} (question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
        """, q[1:])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    insert_sample_questions()
    print("Database and questions created.")
