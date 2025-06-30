import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="ITINEWDB",
        user="ITI",
        password="213712367"
    )

def refresh():
    for row in tree.get_children():
        tree.delete(row)
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to load data:\n{e}")

def add_customer():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO customers (customerid, customername, phone, email, address)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            id_entry.get(),
            name_entry.get(),
            phone_entry.get(),
            email_entry.get(),
            address_entry.get()
        ))
        conn.commit()
        conn.close()
        refresh()
        messagebox.showinfo("Success", "✅ Customer added successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to add customer:\n{e}")

def update_customer():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            UPDATE customers
            SET customername=%s, phone=%s, email=%s, address=%s
            WHERE customerid=%s
        """, (
            name_entry.get(),
            phone_entry.get(),
            email_entry.get(),
            address_entry.get(),
            id_entry.get()
        ))
        conn.commit()
        conn.close()
        refresh()
        messagebox.showinfo("Success", "✅ Customer updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to update customer:\n{e}")

def delete_customer():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM customers WHERE customerid=%s", (id_entry.get(),))
        conn.commit()
        conn.close()
        refresh()
        messagebox.showinfo("Success", "🗑️ Customer deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to delete customer:\n{e}")

def on_select(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        id_entry.insert(0, values[0])
        name_entry.insert(0, values[1])
        phone_entry.insert(0, values[2])
        email_entry.insert(0, values[3])
        address_entry.insert(0, values[4])

# === GUI ===
root = tk.Tk()
root.title("ניהול לקוחות")
root.geometry("900x500")
root.configure(bg="#FADADD")

title = tk.Label(root, text="ניהול לקוחות", font=("Helvetica", 20, "bold"), bg="#FADADD")
title.grid(row=0, column=0, columnspan=6, pady=10)

labels = ["ID", "Name", "Phone", "Email", "Address"]
entries = []

for i, label_text in enumerate(labels):
    lbl = tk.Label(root, text=label_text, bg="#FADADD", font=("Arial", 10, "bold"))
    lbl.grid(row=1, column=i)
    ent = tk.Entry(root)
    ent.grid(row=2, column=i)
    entries.append(ent)

id_entry, name_entry, phone_entry, email_entry, address_entry = entries

tree = ttk.Treeview(root, columns=labels, show="headings", height=15)
for col in labels:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.grid(row=3, column=0, columnspan=6, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", on_select)

btn_add = tk.Button(root, text="➕ הוסף לקוח", command=add_customer)
btn_add.grid(row=4, column=0)

btn_update = tk.Button(root, text="✏️ עדכן לקוח", command=update_customer)
btn_update.grid(row=4, column=1)

btn_delete = tk.Button(root, text="🗑️ מחק לקוח", command=delete_customer)
btn_delete.grid(row=4, column=2)

btn_refresh = tk.Button(root, text="🔄 רענן", command=refresh)
btn_refresh.grid(row=4, column=3)

refresh()
root.mainloop()
