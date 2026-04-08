from models import Task, TaskCreate
from database import connection


# =========================
# CREATE (INSERT)
# =========================
# Takes a TaskCreate object (from FastAPI request body)
# Inserts the task into the database
def create_task(task: TaskCreate):
    conn = connection()            # Open connection to SQLite database
    cur = conn.cursor()            # Create cursor to execute SQL queries
    
    # Insert task into "tasks" table
    cur.execute(
        """
        INSERT INTO tasks
        (task_name, task_desc, assigned_to)
        VALUES (?, ?, ?)
        """,
        (task.task_name, task.task_desc, task.assigned_to)
    )

    conn.commit()                  # Save changes
    conn.close()                   # Close connection

    return task                    # Return the created task (no id yet)


# =========================
# READ (SELECT)
# =========================
# Fetches all tasks from the database and converts them into Task models
def get_tasks() -> list:
    conn = connection()            # Open database connection
    cur = conn.cursor()
    
    # Execute query to get all rows from tasks table
    rows = cur.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    # Convert each row into a Task object (Pydantic model)
    return [
        Task(
            task_id=row["id"],                     # Map DB column "id" → model field "task_id"
            task_name=row["task_name"],
            task_desc=row["task_desc"],
            assigned_to=row["assigned_to"],
            completed=bool(row["completed"])       # Convert 0/1 → False/True
        )
        for row in rows
    ]


# =========================
# UPDATE
# =========================
# Updates an existing task using values from TaskUpdate model
def update_task(task, task_id: int) -> dict:
    conn = connection()
    cur = conn.cursor()

    # Update task with matching id
    cur.execute(
        """
        UPDATE tasks
        SET task_name = ?, task_desc = ?, assigned_to = ?, completed = ?
        WHERE id = ?
        """,
        (
            task.task_name,
            task.task_desc,              
            task.assigned_to,
            int(task.completed),    # Convert bool → 0/1 for SQLite
            task_id            
        )
    )

    conn.commit()
    conn.close()

    return {"message": f"Task id #{task_id} updated"}


# =========================
# DELETE
# =========================
# Deletes a task from the database using its id
def delete_task(task_id: int):
    conn = connection()
    cur = conn.cursor()

    # Delete row where id matches task_id
    cur.execute(
        """
        DELETE FROM tasks
        WHERE id = ?
        """,
        (task_id,)   
    )

    conn.commit()
    conn.close()

    return {"message": f"Task id #{task_id} deleted"}