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

### Next Steps
- [ ] Create CRUD functions (crud.py)
- [ ] Implement `create_task()` (INSERT into SQLite)
- [ ] Implement `get_tasks()` (SELECT from SQLite)
- [ ] Connect FastAPI routes (main.py)

## Next Session Focus

Start with:
- Build `create_task()` in crud.py
- Test inserting a task into database