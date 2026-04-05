from models import Task, TaskCreate
from database import connection

def create_task(task : TaskCreate):
    conn = connection()
    cur = conn.cursor()
    
    cur.execute(
        """
            INSERT INTO tasks
            (task_name, task_desc, assigned_to)
            VALUES (?, ?, ?)
        """,
        (task.task_name, task.task_desc, task.assigned_to)
    )
    conn.commit()
    conn.close()

    return task

def get_tasks() -> list:
    conn = connection()
    cur = conn.cursor()
    
    rows = cur.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return [
        Task(
            task_id = row["id"],
            task_name = row["task_name"],
            task_desc = row["task_desc"],
            assigned_to = row["assigned_to"],
            completed = bool(row["completed"])
        )
        for row in rows
    ]