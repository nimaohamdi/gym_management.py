import sqlite3
import tkinter as tk
from tkinter import messagebox

def create_db():
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

def register_member():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    membership_type = entry_membership_type.get()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()

    conn = sqlite3.connect('gym_management.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO members (name, phone, email, membership_type, start_date, end_date)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (name, phone, email, membership_type, start_date, end_date))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Member registered successfully!")


def add_trainer():
    name = entry_trainer_name.get()
    specialty = entry_trainer_specialty.get()

    conn = sqlite3.connect('gym_management.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO trainers (name, specialty)
                      VALUES (?, ?)''', (name, specialty))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Trainer added successfully!")


def add_class():
    class_name = entry_class_name.get()
    trainer_id = entry_trainer_id.get()
    time = entry_class_time.get()
    capacity = entry_class_capacity.get()

    conn = sqlite3.connect('gym_management.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO classes (class_name, trainer_id, time, capacity)
                      VALUES (?, ?, ?, ?)''', (class_name, trainer_id, time, capacity))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Class added successfully!")


def add_payment():
    member_id = entry_member_id.get()
    amount = entry_amount.get()
    date = entry_payment_date.get()

    conn = sqlite3.connect('gym_management.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO payments (member_id, amount, date)
                      VALUES (?, ?, ?)''', (member_id, amount, date))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Payment added successfully!")


def show_members_report():
    conn = sqlite3.connect('gym_management.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM members''')
    members = cursor.fetchall()

    report_window = tk.Toplevel(root)
    report_window.title("Members Report")

    for index, member in enumerate(members):
        tk.Label(report_window, text=member).grid(row=index)

    conn.close()


root = tk.Tk()
root.title("Gym Management System")


tk.Label(root, text="Name").grid(row=0)
tk.Label(root, text="Phone").grid(row=1)
tk.Label(root, text="Email").grid(row=2)
tk.Label(root, text="Membership Type").grid(row=3)
tk.Label(root, text="Start Date").grid(row=4)
tk.Label(root, text="End Date").grid(row=5)

entry_name = tk.Entry(root)
entry_phone = tk.Entry(root)
entry_email = tk.Entry(root)
entry_membership_type = tk.Entry(root)
entry_start_date = tk.Entry(root)
entry_end_date = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_phone.grid(row=1, column=1)
entry_email.grid(row=2, column=1)
entry_membership_type.grid(row=3, column=1)
entry_start_date.grid(row=4, column=1)
entry_end_date.grid(row=5, column=1)

tk.Button(root, text='Register Member', command=register_member).grid(row=6, column=1)


tk.Label(root, text="Trainer Name").grid(row=7)
tk.Label(root, text="Specialty").grid(row=8)

entry_trainer_name = tk.Entry(root)
entry_trainer_specialty = tk.Entry(root)

entry_trainer_name.grid(row=7, column=1)
entry_trainer_specialty.grid(row=8, column=1)

tk.Button(root, text='Add Trainer', command=add_trainer).grid(row=9, column=1)


tk.Label(root, text="Class Name").grid(row=10)
tk.Label(root, text="Trainer ID").grid(row=11)
tk.Label(root, text="Time").grid(row=12)
tk.Label(root, text="Capacity").grid(row=13)

entry_class_name = tk.Entry(root)
entry_trainer_id = tk.Entry(root)
entry_class_time = tk.Entry(root)
entry_class_capacity = tk.Entry(root)

entry_class_name.grid(row=10, column=1)
entry_trainer_id.grid(row=11, column=1)
entry_class_time.grid(row=12, column=1)
entry_class_capacity.grid(row=13, column=1)

tk.Button(root, text='Add Class', command=add_class).grid(row=14, column=1)


tk.Label(root, text="Member ID").grid(row=15)
tk.Label(root, text="Amount").grid(row=16)
tk.Label(root, text="Payment Date").grid(row=17)

entry_member_id = tk.Entry(root)
entry_amount = tk.Entry(root)
entry_payment_date = tk.Entry(root)

entry_member_id.grid(row=15, column=1)
entry_amount.grid(row=16, column=1)
entry_payment_date.grid(row=17, column=1)

tk.Button(root, text='Add Payment', command=add_payment).grid(row=18, column=1)


tk.Button(root, text='Show Members Report', command=show_members_report).grid(row=19, column=1)

create_db()
root.mainloop()
