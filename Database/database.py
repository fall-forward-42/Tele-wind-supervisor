import sqlite3
def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 description TEXT,
                 remind_time TEXT,  -- ISO 8601 format (YYYY-MM-DDTHH:MM:SS)
                 status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 action TEXT,
                 timestamp TEXT)''')
    conn.commit()
    conn.close()

def add_task(user_id, description, remind_time):
    conn = sqlite3.connect('tasks.db')
    print('add task....')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (user_id, description, remind_time, status) VALUES (?, ?, ?, ?)",
              (user_id, description, remind_time, "pending"))
    print('add task.... done')
    conn.commit()
    conn.close()


def get_tasks(user_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT id, description, remind_time, status FROM tasks WHERE user_id = ?", (user_id,))
    tasks = c.fetchall()
    conn.close()
    return tasks