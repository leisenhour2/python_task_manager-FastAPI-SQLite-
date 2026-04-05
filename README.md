# Python Task Manager (FastAPI + SQLite)

## Description
A task manager API built with FastAPI and SQLite.

## Status
🚧 In Progress

## Goals
- Build REST API
- Store tasks in SQLite database
- Add CRUD functionality

## Installation
```bash
pip install -r requirements.txt
```
## To-Do List

- [x] Setup database (database.py)
- [x] Create Pydantic models (models.py)

### Core Features
- [x] Implement `create_task()` (INSERT into SQLite)
- [x] Implement `get_tasks()` (SELECT from SQLite)
- [x] Create CRUD functions (crud.py)
- [x] Connect FastAPI routes (main.py)

### Next Steps
- [ ] Implement `update_task()` (UPDATE SQLite)
- [ ] Implement `delete_task()` (DELETE FROM SQLite)

## Next Session Focus

Start with:
- Build `update_task()` in crud.py
- Test updating a task into database
- Build `delete_task()` in crud.py
- Test deleting a task from database