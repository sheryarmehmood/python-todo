# Todo App Overview

## What This App Does

This is a simple Python todo list app. The browser shows a todo list UI where the user can:

- Add a new task
- Mark a task as complete or incomplete
- Edit a task title
- Delete a task

The frontend is built with HTML, CSS, and JavaScript. The backend is built with Python's built-in `http.server`. The data is stored in a MySQL database.

## File Guide

### `index.html`

This is the main page of the app.

It contains:

- The page title
- The `ToDo List!` heading
- The input field for entering a task
- The add button
- The empty `tasks` container where JavaScript inserts todo items
- Links to `style.css` and `script.js`

### `style.css`

This file controls the design of the frontend.

It styles:

- The page background
- The centered todo container
- The title
- The input row
- The purple add button
- Each task row
- The green complete button
- The yellow edit button
- The red delete button
- The completed task line-through style
- The mobile layout for small screens

### `script.js`

This is the frontend logic.

Important functions:

- `loadTasks()` gets tasks from `/tasks` and displays them on the page.
- `addTask()` sends a new task to `/add-task`.
- `toggleTask(id)` marks a task complete or incomplete through `/toggle-task`.
- `editTask(task)` updates a task title through `/update-task`.
- `deleteTask(id)` deletes a task through `/delete-task`.
- `createActionButton()` creates the icon buttons used in every task row.

When the page loads, `loadTasks()` runs automatically. The Enter key also adds a task from the input field.

### `server.py`

This is the Python backend server.

It does two jobs:

1. Serves frontend files:
   - `/` returns `index.html`
   - `/style.css` returns the CSS file
   - `/script.js` returns the JavaScript file

2. Handles API routes:
   - `GET /tasks` returns all tasks as JSON
   - `POST /add-task` adds a task
   - `POST /toggle-task` completes or uncompletes a task
   - `POST /update-task` edits a task title
   - `POST /delete-task` deletes a task

The server runs on:

```text
http://localhost:8000
```

### `db.py`

This file handles the MySQL database.

Important functions:

- `get_connection()` connects to MySQL.
- `setup_database()` creates the `tasks` table if it does not exist and adds the `completed` column if needed.
- `get_tasks()` reads all tasks from the database.
- `add_task(title)` inserts a new task.
- `toggle_task(task_id)` changes the completed status.
- `update_task(task_id, title)` edits a task title.
- `delete_task(task_id)` removes a task.

The app expects a MySQL database named `todo_app`.

### `test.py`

This is a small database connection test.

It imports `get_connection()` from `db.py`, connects to MySQL, prints `Connected Successfully`, and closes the connection.

## Frontend And Backend Flow

1. User opens `http://localhost:8000`.
2. `server.py` sends `index.html`.
3. The browser loads `style.css` and `script.js`.
4. `script.js` calls `GET /tasks`.
5. `server.py` asks `db.py` for tasks.
6. `db.py` reads tasks from MySQL.
7. The tasks are returned to JavaScript as JSON.
8. JavaScript displays the tasks in the page.

When the user adds, edits, completes, or deletes a task, JavaScript sends a `POST` request to the backend. The backend updates MySQL, then JavaScript reloads the task list.

## How To Run

Start the server:

```bash
python server.py
```

Then open:

```text
http://localhost:8000
```

To test only the database connection:

```bash
python test.py
```
