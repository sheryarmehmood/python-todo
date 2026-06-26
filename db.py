import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root_mysql_2026",
        database="todo_app"
    )


def setup_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            completed TINYINT(1) NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("SHOW COLUMNS FROM tasks LIKE 'completed'")

    if cursor.fetchone() is None:

        cursor.execute("""
            ALTER TABLE tasks
            ADD completed TINYINT(1) NOT NULL DEFAULT 0
        """)

    conn.commit()

    conn.close()


def get_tasks():

    setup_database()

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id,
            title,
            completed
        FROM tasks
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    conn.close()

    return [
        {
            "id": task["id"],
            "title": task["title"],
            "completed": task["completed"] == 1
        }
        for task in tasks
    ]


def add_task(title):

    setup_database()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(title) VALUES(%s)",
        (title,)
    )

    conn.commit()

    conn.close()


def toggle_task(task_id):

    setup_database()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET completed = NOT completed
        WHERE id = %s
        """,
        (task_id,)
    )

    conn.commit()

    conn.close()


def update_task(task_id, title):

    setup_database()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET title = %s WHERE id = %s",
        (title, task_id)
    )

    conn.commit()

    conn.close()


def delete_task(task_id):

    setup_database()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    conn.commit()

    conn.close()
