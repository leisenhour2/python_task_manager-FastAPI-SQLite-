from pathlib import Path
import sqlite3 as sql

# Setup Filepaths
MAIN_DIR: Path = Path(__file__).resolve().parent
DB_DIR: Path = MAIN_DIR / "db"

# Makes sure 'DB_DIR("/db")' exists and creates it if it doesn't
DB_DIR.mkdir(parents=True, exist_ok=True)

# Path to SQLite database file
DB_FILE: Path = DB_DIR / "tasks.db"

# Function that connects user to database
def connection():
    # Establish connection to SQLite database file
    conn = sql.connect(DB_FILE)
    conn.row_factory = sql.Row  # Returns dict-like rows
    return conn


# Function that creates the table
def create_table():
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            task_desc TEXT NOT NULL,
            assigned_to TEXT NOT NULL,
            completed INTEGER DEFAULT 0 CHECK (completed IN (0, 1))
        )
        """
    )

    conn.commit()
    conn.close()

    # Confirms table creation + shows DB location
    print(f"Tasks table ready at: {DB_FILE}")


# Executes table creation function ONLY when run directly
if __name__ == "__main__":
    create_table()