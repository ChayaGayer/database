import tkinter as tk
from tkinter import messagebox
import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="ITINEWDB",
        user="ITI",
        password="213712367"
    )

def count_shifts():
    worker_id = entry_worker_id.get()
    if not worker_id.isdigit():
        messagebox.showerror("שגיאה", "אנא הכנס מספר עובד חוקי")
        return

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT count_worker_shifts(%s)", (worker_id,))
        result = cursor.fetchone()[0]
        messagebox.showinfo("תוצאה", f"לעובד מספר {worker_id} יש {result} משמרות.")
        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("שגיאה", f"שגיאה בחיבור או בשאילתה:\n{e}")

# GUI
window = tk.Tk()
window.title("בדיקת כמות משמרות לעובד")
window.configure(bg="#fddde6")
window.geometry("400x300")  # הגדלת החלון

tk.Label(window, text="בדיקת כמות משמרות", font=("Arial", 18, "bold"), bg="#fddde6", fg="black").pack(pady=20)

frame = tk.Frame(window, bg="#fddde6")
frame.pack(pady=10)

tk.Label(frame, text="הכנס worker_id:", font=("Arial", 12), bg="#fddde6").grid(row=0, column=0, padx=10, pady=10)
entry_worker_id = tk.Entry(frame, font=("Arial", 12))
entry_worker_id.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(window, text="בדוק כמות משמרות", font=("Arial", 12, "bold"),
                   bg="black", fg="white", width=25, height=2, command=count_shifts)
button.pack(pady=20)

window.mainloop()
