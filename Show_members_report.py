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
