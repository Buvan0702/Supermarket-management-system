import tkinter as tk
from tkinter import messagebox
import mysql.connector
from database_config import get_db_connection

# Function to register the user
def register_user():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not first_name or not last_name or not email or not password:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    # Insert user data into the database
    try:
        connection = get_db_connection()
        if connection is None:
            return  # Stop if no connection is made

        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, password))
        connection.commit()

        cursor.close()
        connection.close()
        
        messagebox.showinfo("Registration Success", "User registered successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("SuperMarket - Sign Up")
root.geometry("800x500")  # Fixed window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="#f2f2f2")  # Light gray background

# ---------------- Main Frame (Holds everything) ----------------
main_frame = tk.Frame(root, bg="white", relief="flat")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=420)

# ---------------- Registration Form ----------------
registration_frame = tk.Frame(main_frame, bg="white", width=350, height=420)
registration_frame.pack(side="left", fill="both", padx=20, pady=20)

tk.Label(registration_frame, text="SuperMarket", font=("Arial", 20, "bold"), fg="#2563eb", bg="white").pack(anchor="w")
tk.Label(registration_frame, text="Register to start shopping!", font=("Arial", 10), bg="white", fg="gray").pack(anchor="w", pady=5)

tk.Label(registration_frame, text="Enter your details", font=("Arial", 11, "bold"), bg="white").pack(anchor="w", pady=(20, 0))

# --- First Name Entry ---
tk.Label(registration_frame, text="First Name", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(15, 0))
first_name_entry = tk.Entry(registration_frame, font=("Arial", 12), bg="white", relief="solid", bd=1)
first_name_entry.pack(fill="x", ipady=5, pady=2)

# --- Last Name Entry ---
tk.Label(registration_frame, text="Last Name", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
last_name_entry = tk.Entry(registration_frame, font=("Arial", 12), bg="white", relief="solid", bd=1)
last_name_entry.pack(fill="x", ipady=5, pady=2)

# --- Email Entry --- 
tk.Label(registration_frame, text="Email", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
email_entry = tk.Entry(registration_frame, font=("Arial", 12), bg="white", relief="solid", bd=1)
email_entry.pack(fill="x", ipady=5, pady=2)

# --- Password Entry --- 
tk.Label(registration_frame, text="Password", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
password_entry = tk.Entry(registration_frame, show="*", font=("Arial", 12), bg="white", relief="solid", bd=1)
password_entry.pack(fill="x", ipady=5, pady=2)

# --- Register Button --- 
register_btn = tk.Button(registration_frame, text="Register", font=("Arial", 12, "bold"), bg="#2563eb", fg="white",
                         relief="flat", cursor="hand2", height=2, activebackground="#1d4ed8", command=register_user)
register_btn.pack(fill="x", pady=(15, 10))

# ---------------- Run Application ----------------
root.mainloop()
