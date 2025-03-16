import tkinter as tk
from tkinter import ttk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("SuperMarket - Checkout")
root.geometry("900x500")  # Adjusted height for proper spacing
root.resizable(False, False)  # Prevent resizing
root.configure(bg="#f2f2f2")  # Light gray background

# ---------------- Sidebar (Blue Navigation Menu) ----------------
sidebar = tk.Frame(root, bg="#2563eb", width=180, height=500)
sidebar.pack(side="left", fill="y")

# Sidebar Title
tk.Label(sidebar, text="SuperMarket", font=("Arial", 14, "bold"), fg="white", bg="#2563eb", anchor="w").pack(pady=20, padx=20)

# Sidebar Buttons
menu_items = ["Home", "Cart", "Previous Orders", "Logout"]
for item in menu_items:
    btn = tk.Button(sidebar, text=item, font=("Arial", 11), fg="white", bg="#2563eb",
                    relief="flat", anchor="w", padx=20, activebackground="#1d4ed8", bd=0)
    btn.pack(fill="x", pady=3)

# ---------------- Main Content ----------------
main_content = tk.Frame(root, bg="#f2f2f2")
main_content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Header
header_frame = tk.Frame(main_content, bg="#f2f2f2")
header_frame.pack(fill="x")

tk.Label(header_frame, text="Checkout", font=("Arial", 16, "bold"), fg="#2563eb", bg="#f2f2f2").pack(side="left")

# Search Bar with Refresh Icon
search_frame = tk.Frame(header_frame, bg="#f2f2f2")
search_frame.pack(side="right")

refresh_icon = tk.Button(search_frame, text="🔄", font=("Arial", 10), bg="#e0e0e0", relief="flat", cursor="hand2")
refresh_icon.pack(side="left", padx=5)

search_entry = tk.Entry(search_frame, font=("Arial", 11), bg="white", relief="solid", bd=1)
search_entry.insert(0, "Search...")  # Placeholder text
search_entry.pack(side="left", ipadx=10, ipady=3)

# ---------------- Cart Items Section ----------------
cart_section = tk.Frame(main_content, bg="#f2f2f2")
cart_section.pack(fill="x", pady=10)

cart_frame = tk.Frame(cart_section, bg="white", relief="ridge", bd=1)
cart_frame.pack(fill="x")

tk.Label(cart_frame, text="Your Cart Items", font=("Arial", 11, "bold"), bg="white", pady=8, padx=10).pack(anchor="w")

cart_items = [
    {"name": "Fresh Apples", "price": "$2.00"},
    {"name": "Organic Bananas", "price": "$1.50"},
    {"name": "Fresh Broccoli", "price": "$1.80"}
]

for item in cart_items:
    item_row = tk.Frame(cart_frame, bg="white")
    item_row.pack(fill="x", padx=10, pady=3)

    tk.Label(item_row, text=item["name"], font=("Arial", 10), bg="white", anchor="w").pack(side="left")
    tk.Label(item_row, text=item["price"], font=("Arial", 10), bg="white", anchor="e").pack(side="right")

# Total Row
total_row = tk.Frame(cart_frame, bg="white")
total_row.pack(fill="x", padx=10, pady=8)

tk.Label(total_row, text="Total:", font=("Arial", 10, "bold"), bg="white", anchor="w").pack(side="left")
tk.Label(total_row, text="$5.30", font=("Arial", 10, "bold"), fg="black", bg="white", anchor="e").pack(side="right")

# ---------------- Buttons (Edit & Delete) ----------------
buttons_section = tk.Frame(main_content, bg="#f2f2f2")
buttons_section.pack(fill="x", pady=20)

edit_button = tk.Button(buttons_section, text="Edit", font=("Arial", 11, "bold"), bg="#f97316", fg="white",
                        relief="flat", cursor="hand2", width=10, activebackground="#ea580c")
edit_button.pack(side="left", padx=20)

delete_button = tk.Button(buttons_section, text="Delete", font=("Arial", 11, "bold"), bg="#dc2626", fg="white",
                          relief="flat", cursor="hand2", width=10, activebackground="#b91c1c")
delete_button.pack(side="right", padx=20)

# ---------------- Run Application ----------------
root.mainloop()
