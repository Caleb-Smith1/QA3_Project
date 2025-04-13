import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

tables = ["database_admin", "microeconomics", "business_mgmt", "statistics", "app_dev"]

for table in tables:
    print(f"Cleaning duplicates in {table}...")
    cursor.execute(f"""
        DELETE FROM {table}
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM {table}
            GROUP BY question
        )
    """)

conn.commit()
conn.close()
print("✅ Duplicate questions removed.")
