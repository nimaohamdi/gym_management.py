import sqlite3


conn = sqlite3.connect('gym_management.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    membership_type TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS trainers (
    trainer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL,
    trainer_id INTEGER NOT NULL,
    time TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    FOREIGN KEY(trainer_id) REFERENCES trainers(trainer_id)
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY(member_id) REFERENCES members(member_id)
)''')

conn.commit()
conn.close()
