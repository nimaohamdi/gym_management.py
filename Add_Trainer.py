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
