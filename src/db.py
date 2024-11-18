import sqlite3


def create_table():
    """Create the exams table if it doesn't exist."""
    con = sqlite3.connect("src/scores.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS exams (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            score TEXT, 
            date TEXT
        )
    """)
    con.commit()
    con.close()


def add_exam_to_db(id, name, score, date):
    """Insert a new exam record into the database."""
    con = sqlite3.connect("src/scores.db")
    cur = con.cursor()

    # Use parameterized queries to prevent SQL injection
    cur.execute("""
        INSERT INTO exams (id, name, score, date) 
        VALUES (?, ?, ?, ?)
    """, (id, name, score, date))

    # Commit the transaction and close the connection
    con.commit()
    con.close()



