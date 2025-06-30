import tkinter as tk
from tkinter import messagebox
import psycopg2

# === חיבור למסד הנתונים ===
def connect():
    return psycopg2.connect(
        host="localhost",
        database="ITINEWDB",
        user="ITI",
        password="213712367"
    )

# === שאילתה 1: סכום כולל ללקוח ===
def total_orders_by_customer():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT c.CustomerName, COUNT(o.OrderID) AS OrderCount, SUM(o.TotalAmount) AS TotalSpent
            FROM customers c
            JOIN Orders o ON c.CustomerID = o.CustomerID
            GROUP BY c.CustomerName
            ORDER BY TotalSpent DESC
        ''')
        rows = cur.fetchall()
        output = "\n".join([f"{row[0]} | Orders: {row[1]} | Total: {row[2]}" for row in rows])
        messagebox.showinfo("Total Orders per Customer", output)
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("שגיאה", str(e))

# === שאילתה 2: מספר עובדים לפי סטטוס ===
def count_workers_by_status():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT wstatus, COUNT(*) 
            FROM worker
            GROUP BY wstatus
            ORDER BY COUNT(*) DESC
        ''')
        rows = cur.fetchall()
        output = "\n".join([f"Status: {row[0]} | Count: {row[1]}" for row in rows])
        messagebox.showinfo("Worker Count by Status", output)
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("שגיאה", str(e))

# === פונקציה: סך שכר לפי סטטוס ===
def salary_by_status():
    try:
        status = status_entry.get()
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT total_salary_by_status(%s)", (status,))
        total = cur.fetchone()[0]
        messagebox.showinfo("Total Salary", f"Total salary for status '{status}': {total}")
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("שגיאה", str(e))

# === פרוצדורה: שיוך עובד למשמרת ===
def assign_worker():
    try:
        wid = int(worker_id_entry.get())
        sid = int(shift_id_entry.get())
        conn = connect()
        cur = conn.cursor()
        cur.execute("CALL assign_worker_to_shift(%s, %s)", (wid, sid))
        conn.commit()
        messagebox.showinfo("Success", f"Worker {wid} assigned to shift {sid}.")
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("שגיאה", str(e))

# === GUI ===
root = tk.Tk()
root.title("Queries & Functions")
root.geometry("480x420")
root.configure(bg="#fcdde4")  # רקע ורוד בהיר

# פונקציות עיצוב
def styled_button(master, text, command):
    return tk.Button(master, text=text, command=command,
                     font=("Arial", 12, "bold"),
                     bg="black", fg="white", width=35,
                     relief="raised", bd=4)

def styled_label(master, text):
    return tk.Label(master, text=text, font=("Arial", 12), bg="#fcdde4")

def styled_entry(master, width=20):
    return tk.Entry(master, font=("Arial", 12), width=width)

# כפתור 1: סך ההזמנות ללקוח
styled_button(root, "Total Orders per Customer", total_orders_by_customer).pack(pady=10)

# כפתור 2: מספר עובדים לפי סטטוס
styled_button(root, "Count Workers by Status", count_workers_by_status).pack(pady=10)

# שדה סטטוס עובד
status_frame = tk.Frame(root, bg="#fcdde4")
styled_label(status_frame, "Worker Status:").pack(side=tk.LEFT)
status_entry = styled_entry(status_frame)
status_entry.pack(side=tk.LEFT, padx=5)
status_frame.pack(pady=10)

# כפתור 3: חישוב שכר לפי סטטוס
styled_button(root, "Total Salary by Status", salary_by_status).pack(pady=10)

# שיוך עובד למשמרת
assign_frame = tk.Frame(root, bg="#fcdde4")
styled_label(assign_frame, "Worker ID:").grid(row=0, column=0, padx=5)
worker_id_entry = styled_entry(assign_frame, width=6)
worker_id_entry.grid(row=0, column=1, padx=5)

styled_label(assign_frame, "Shift ID:").grid(row=0, column=2, padx=5)
shift_id_entry = styled_entry(assign_frame, width=6)
shift_id_entry.grid(row=0, column=3, padx=5)

assign_frame.pack(pady=10)

# כפתור 4: שיוך עובד למשמרת
styled_button(root, "Assign Worker to Shift", assign_worker).pack(pady=10)

root.mainloop()
