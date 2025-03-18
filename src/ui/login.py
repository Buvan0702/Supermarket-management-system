import tkinter as tk
import mysql.connector
from tkinter import messagebox
from database_config import get_db_connection

# Function to check login credentials
def check_login():
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showwarning("Input Error", "Please fill out both email and password.")
        return

    # Check credentials in the database
    try:
        connection = get_db_connection()
        if connection is None:
            return  # Stop if no connection is made

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        # If user is found and password matches
        if user and user[3] == password:  # Assuming password is stored in index 3
            messagebox.showinfo("Login Success", "Login successful!")
            # You can add functionality to open the next window or perform any action after login
        else:
            messagebox.showerror("Login Failed", "Invalid email or password!")
        
        cursor.close()
        connection.close()
    
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("SuperMarket - Login")
root.geometry("800x500")  # Fixed window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="#f2f2f2")  # Light gray background

# ---------------- Main Frame (Holds everything) ----------------
main_frame = tk.Frame(root, bg="white", relief="flat")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=420)  # Increased height to 420

# ---------------- Left Side - Login Form ----------------
left_frame = tk.Frame(main_frame, bg="white", width=350, height=420)
left_frame.pack(side="left", fill="both", padx=20, pady=20)

tk.Label(left_frame, text="SuperMarket", font=("Arial", 20, "bold"), fg="#2563eb", bg="white").pack(anchor="w")
tk.Label(left_frame, text="Manage your shopping experience seamlessly.", 
         font=("Arial", 10), bg="white", fg="gray").pack(anchor="w", pady=5)

tk.Label(left_frame, text="Enter your login details", font=("Arial", 11, "bold"), bg="white").pack(anchor="w", pady=(20, 0))
tk.Label(left_frame, text="Enter the registered credentials used while signing up", font=("Arial", 9), 
         bg="white", fg="gray").pack(anchor="w")

# --- Email Entry --- 
tk.Label(left_frame, text="Email", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(15, 0))
email_entry = tk.Entry(left_frame, font=("Arial", 12), bg="white", relief="solid", bd=1)
email_entry.pack(fill="x", ipady=5, pady=2)

# --- Password Entry --- 
tk.Label(left_frame, text="Password", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
password_entry = tk.Entry(left_frame, show="*", font=("Arial", 12), bg="white", relief="solid", bd=1)
password_entry.pack(fill="x", ipady=5, pady=2)

# --- Login Button --- 
login_btn = tk.Button(left_frame, text="Login", font=("Arial", 12, "bold"), bg="#2563eb", fg="white",
                       relief="flat", cursor="hand2", height=2, activebackground="#1d4ed8", command=check_login)
login_btn.pack(fill="x", pady=(15, 10))

# ---------------- Run Application ----------------
root.mainloop()
