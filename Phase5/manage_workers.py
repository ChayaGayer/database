import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

# === הגדרת חיבור למסד הנתונים ===
def connect():
    return psycopg2.connect(
        host="localhost",
        database="ITINEWDB",
        user="ITI",
        password="213712367"
    )

# === רענון נתונים מהטבלה ===
def refresh():
    for row in tree.get_children():
        tree.delete(row)
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT wid, wfirstname, wlastname, salary, wseniority, wstatus, havebonus FROM worker")
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to load data:\n{e}")

# === הוספת עובד חדש ===
def add_worker():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO worker (wid, wfirstname, wlastname, salary, wseniority, wstatus, havebonus)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            wid_entry.get(),
            wfirstname_entry.get(),
            wlastname_entry.get(),
            salary_entry.get(),
            wseniority_entry.get(),
            wstatus_entry.get(),
            havebonus_entry.get()
        ))
        conn.commit()
        conn.close()
        refresh()
        messagebox.showinfo("Success", "✅ Worker added successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to add worker:\n{e}")

# === עדכון עובד ===
def update_worker():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE worker
            SET wfirstname=%s, wlastname=%s, salary=%s, wseniority=%s, wstatus=%s, havebonus=%s
            WHERE wid=%s
        """, (
            wfirstname_entry.get(),
            wlastname_entry.get(),
            salary_entry.get(),
            wseniority_entry.get(),
            wstatus_entry.get(),
            havebonus_entry.get(),
            wid_entry.get()
        ))
        conn.commit()
        conn.close()
        refresh()
        messagebox.showinfo("Success", "✏️ Worker updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to update worker:\n{e}")

# === מחיקת עובד ===
def delete_worker():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM worker WHERE wid=%s", (wid_entry.get(),))
        conn.commit()
        conn.close()
        refresh()
        messagebox.showinfo("Success", "🗑️ Worker deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to delete worker:\n{e}")

# === טעינת עובד לטופס בעת לחיצה בטבלה ===
def on_select(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        for entry, value in zip(entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

# === GUI עיצוב ===
root = tk.Tk()
root.title("ניהול עובדים")
root.configure(bg="#ffe6ea")
root.geometry("950x550")

labels = ["ID", "First Name", "Last Name", "Salary", "Seniority", "Status", "Bonus"]
entries = []

for i, label_text in enumerate(labels):
    lbl = tk.Label(root, text=label_text, bg="#ffe6ea", font=("Arial", 10, "bold"))
    lbl.grid(row=0, column=i, padx=5, pady=5)
    ent = tk.Entry(root)
    ent.grid(row=1, column=i, padx=5, pady=5)
    entries.append(ent)

(wid_entry, wfirstname_entry, wlastname_entry,
 salary_entry, wseniority_entry, wstatus_entry,
 havebonus_entry) = entries

tree = ttk.Treeview(root, columns=labels, show="headings", height=15)
for col in labels:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.grid(row=2, column=0, columnspan=7, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", on_select)

# === כפתורים ===
btn_add = tk.Button(root, text="➕ הוסף עובד", command=add_worker)
btn_add.grid(row=3, column=0, pady=10)

btn_update = tk.Button(root, text="✏️ עדכן עובד", command=update_worker)
btn_update.grid(row=3, column=1)

btn_delete = tk.Button(root, text="🗑️ מחק עובד", command=delete_worker)
btn_delete.grid(row=3, column=2)

btn_refresh = tk.Button(root, text="🔄 רענן", command=refresh)
btn_refresh.grid(row=3, column=3)

refresh()
root.mainloop()
