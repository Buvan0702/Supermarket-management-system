import tkinter as tk
from tkinter import ttk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("User Management System")
root.geometry("900x500")  # Fixed window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg="#333333")  # Dark gray background

# ---------------- Main Container Frame ----------------
container = tk.Frame(root, bg="white")
container.place(relx=0.5, rely=0.5, anchor="center", width=750, height=420)

# ---------------- Sidebar (Blue Admin Panel) ----------------
sidebar = tk.Frame(container, bg="#2563eb", width=180, height=420)
sidebar.pack(side="left", fill="y")

# Sidebar Title
tk.Label(sidebar, text="Admin Panel", font=("Arial", 14, "bold"), fg="white", bg="#2563eb", anchor="w").pack(pady=20, padx=20)

# Sidebar Buttons
menu_items = ["Manage Inventory", "Manage Users", "Generate Report", "Logout"]
for item in menu_items:
    btn = tk.Button(sidebar, text=item, font=("Arial", 11), fg="white", bg="#2563eb",
                    relief="flat", anchor="w", padx=20, activebackground="#1d4ed8", bd=0)
    btn.pack(fill="x", pady=3)

# ---------------- Main Content ----------------
main_content = tk.Frame(container, bg="#f2f2f2")
main_content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Header
tk.Label(main_content, text="User Management", font=("Arial", 16, "bold"), fg="black", bg="#f2f2f2").pack(anchor="w")

# ---------------- Add New User Section ----------------
add_user_frame = tk.Frame(main_content, bg="white", relief="ridge", bd=1)
add_user_frame.pack(fill="x", pady=10, padx=5, ipadx=5, ipady=10)

tk.Label(add_user_frame, text="Add New User", font=("Arial", 11, "bold"), bg="white", pady=5, padx=10).pack(anchor="w")

entry_style = {"font": ("Arial", 11), "bg": "#f8f8f8", "relief": "solid", "bd": 1}

full_name_entry = tk.Entry(add_user_frame, **entry_style)
full_name_entry.insert(0, "Full Name")
full_name_entry.pack(fill="x", padx=10, pady=2, ipady=5)

email_entry = tk.Entry(add_user_frame, **entry_style)
email_entry.insert(0, "Email")
email_entry.pack(fill="x", padx=10, pady=2, ipady=5)

role_entry = tk.Entry(add_user_frame, **entry_style)
role_entry.insert(0, "User Role")
role_entry.pack(fill="x", padx=10, pady=2, ipady=5)

add_user_btn = tk.Button(add_user_frame, text="Add User", font=("Arial", 11, "bold"), bg="#16a34a", fg="white",
                         relief="flat", cursor="hand2", activebackground="#15803d")
add_user_btn.pack(pady=10, padx=10, ipadx=10)

# ---------------- Existing Users Section ----------------
users_frame = tk.Frame(main_content, bg="#f2f2f2")
users_frame.pack(fill="x", pady=10)

tk.Label(users_frame, text="Existing Users", font=("Arial", 11, "bold"), bg="#f2f2f2").pack(anchor="w")

# Users Table
table_frame = tk.Frame(users_frame, bg="white", relief="ridge", bd=1)
table_frame.pack(fill="x", pady=5, padx=5)

columns = ("Name", "Email", "Role", "Actions")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=3)

# Define column headings
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.heading("Role", text="Role")
tree.heading("Actions", text="Actions")

# Define column widths
tree.column("Name", width=200, anchor="w")
tree.column("Email", width=200, anchor="w")
tree.column("Role", width=100, anchor="center")
tree.column("Actions", width=200, anchor="center")

# Insert dummy data
data = [
    ("John Doe", "johndoe@example.com", "Admin"),
    ("Jane Smith", "janesmith@example.com", "Customer")
]

for user in data:
    tree.insert("", "end", values=user)

tree.pack(fill="x")

# ---------------- Run Application ----------------
root.mainloop()
