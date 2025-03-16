import tkinter as tk
from tkinter import ttk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("Inventory Management System")
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
tk.Label(main_content, text="Inventory Management", font=("Arial", 16, "bold"), fg="#2563eb", bg="#f2f2f2").pack(anchor="w")

# ---------------- Add New Item Section ----------------
add_item_frame = tk.Frame(main_content, bg="white", relief="ridge", bd=1)
add_item_frame.pack(fill="x", pady=10, padx=5, ipadx=5, ipady=10)

tk.Label(add_item_frame, text="Add New Item", font=("Arial", 11, "bold"), bg="white", pady=5, padx=10).pack(anchor="w")

entry_style = {"font": ("Arial", 11), "bg": "#f8f8f8", "relief": "solid", "bd": 1}

item_name_entry = tk.Entry(add_item_frame, **entry_style)
item_name_entry.insert(0, "Item Name")
item_name_entry.pack(fill="x", padx=10, pady=2, ipady=5)

price_entry = tk.Entry(add_item_frame, **entry_style)
price_entry.insert(0, "Price ($)")
price_entry.pack(fill="x", padx=10, pady=2, ipady=5)

stock_entry = tk.Entry(add_item_frame, **entry_style)
stock_entry.insert(0, "Stock Quantity")
stock_entry.pack(fill="x", padx=10, pady=2, ipady=5)

add_item_btn = tk.Button(add_item_frame, text="Add Item", font=("Arial", 11, "bold"), bg="#16a34a", fg="white",
                         relief="flat", cursor="hand2", activebackground="#15803d")
add_item_btn.pack(pady=10, padx=10, ipadx=10)

# ---------------- Existing Inventory Section ----------------
inventory_frame = tk.Frame(main_content, bg="#f2f2f2")
inventory_frame.pack(fill="x", pady=10)

tk.Label(inventory_frame, text="Existing Inventory", font=("Arial", 11, "bold"), bg="#f2f2f2").pack(anchor="w")

# Inventory Table
table_frame = tk.Frame(inventory_frame, bg="white", relief="ridge", bd=1)
table_frame.pack(fill="x", pady=5, padx=5)

columns = ("Item Name", "Price", "Stock", "Actions")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=3)

# Define column headings
tree.heading("Item Name", text="Item Name")
tree.heading("Price", text="Price")
tree.heading("Stock", text="Stock")
tree.heading("Actions", text="Actions")

# Define column widths
tree.column("Item Name", width=200, anchor="w")
tree.column("Price", width=100, anchor="center")
tree.column("Stock", width=100, anchor="center")
tree.column("Actions", width=200, anchor="center")

# Insert dummy data
data = [
    ("Fresh Apples", "$2.00", "50"),
    ("Organic Bananas", "$1.50", "30")
]

for item in data:
    tree.insert("", "end", values=item)

tree.pack(fill="x")

# Buttons for actions
for row in tree.get_children():
    tree.insert(row, "end", values=(" ", " ", " ", "Edit  Delete"))

# ---------------- Run Application ----------------
root.mainloop()
