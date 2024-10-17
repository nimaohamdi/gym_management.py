import tkinter as tk
from tkinter import messagebox
import sqlite3

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

root.mainloop()
