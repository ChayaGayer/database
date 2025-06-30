from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
import subprocess

root = Tk()
root.title("🍽️ מערכת ניהול המסעדה")
root.geometry("600x750")
root.configure(bg="#ffeef2")  # רקע ורוד בהיר

# --- לוגו ---
try:
    img = Image.open("logo.png")  # 
    img = img.resize((160, 160))
    logo = ImageTk.PhotoImage(img)
    logo_label = Label(root, image=logo, bg="#ffeef2")
    logo_label.image = logo
    logo_label.pack(pady=10)
except Exception as e:
    print("שגיאה בטעינת הלוגו:", e)

# --- כותרת ---
Label(
    root,
    text="ברוכים הבאים למערכת",
    font=("Arial", 24, "bold"),
    bg="#ffeef2",
    fg="#4c4c4c"
).pack(pady=10)

# --- מסגרת עיצובית מרכזית ---
button_frame = Frame(root, bg="#ffeef2")
button_frame.pack(pady=20)

btn_style = {
    "width": 30,
    "height": 2,
    "font": ("Arial", 12, "bold"),
    "bg": "black",
    "fg": "white"
}

# --- פעולות למסכים ---
def open_workers():
    subprocess.Popen(["python", "manage_workers.py"], shell=True)

def open_customers():
    subprocess.Popen(["python", "manage_customers.py"], shell=True)

def open_scheduled():
    subprocess.Popen(["python", "manage_scheduled.py"], shell=True)

def open_queries():
    subprocess.Popen(["python", "queries_functions_gui.py"], shell=True)

def close_app():
    root.destroy()

# --- כפתורים ---
Button(button_frame, text="👷 ניהול עובדים", command=open_workers, **btn_style).pack(pady=8)
Button(button_frame, text="👥 ניהול לקוחות", command=open_customers, **btn_style).pack(pady=8)
Button(button_frame, text="🛠 שיוך עובד למשמרת", command=open_scheduled, **btn_style).pack(pady=8)
Button(button_frame, text="📊 שאילתות ופרוצדורות", command=open_queries, **btn_style).pack(pady=8)
Button(button_frame, text="🚪 יציאה מהמערכת", command=close_app, **btn_style).pack(pady=30)

root.mainloop()

