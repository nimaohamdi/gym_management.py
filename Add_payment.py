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
