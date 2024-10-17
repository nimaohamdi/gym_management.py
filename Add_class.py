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
