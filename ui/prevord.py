import tkinter as tk
from tkinter import ttk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("SuperMarket - Previous Orders")
root.geometry("900x500")  # Fixed window size
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
tk.Label(main_content, text="Previous Orders", font=("Arial", 16, "bold"), fg="#2563eb", bg="#f2f2f2").pack(anchor="w")

# ---------------- Scrollable Orders Section ----------------
orders_frame_container = tk.Frame(main_content, bg="#f2f2f2")
orders_frame_container.pack(fill="both", expand=True, pady=10)

canvas = tk.Canvas(orders_frame_container, bg="#f2f2f2", highlightthickness=0)
scrollbar = tk.Scrollbar(orders_frame_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f2f2f2")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ---------------- Orders Data ----------------
orders = [
    {
        "order_no": "Order #1",
        "items": [
            ("Fresh Apples", "$2.00"),
            ("Organic Bananas", "$1.50"),
            ("Fresh Broccoli", "$1.80")
        ],
        "total": "$5.30"
    },
    {
        "order_no": "Order #2",
        "items": [
            ("Whole Wheat Bread", "$2.50"),
            ("Almond Milk", "$3.00"),
            ("Eggs", "$2.00")
        ],
        "total": "$7.50"
    },
    {
        "order_no": "Order #3",
        "items": [
            ("Chicken Breast", "$8.00"),
            ("Brown Rice", "$2.00"),
            ("Broccoli", "$1.80")
        ],
        "total": "$11.80"
    },
    {
        "order_no": "Order #4",
        "items": [
            ("Carrots", "$1.00"),
            ("Spinach", "$2.50"),
            ("Avocado", "$3.00")
        ],
        "total": "$6.50"
    },
    {
        "order_no": "Order #5",
        "items": [
            ("Milk", "$3.00"),
            ("Cheese", "$4.00"),
            ("Yogurt", "$2.50")
        ],
        "total": "$9.50"
    }
]

# ---------------- Creating Order Boxes ----------------
for order in orders:
    order_frame = tk.Frame(scrollable_frame, bg="white", relief="ridge", bd=1)
    order_frame.pack(fill="x", pady=10, padx=5, ipadx=5, ipady=5)

    # Order Title
    tk.Label(order_frame, text=order["order_no"], font=("Arial", 11, "bold"), bg="white", pady=5, padx=10).pack(anchor="w")

    # Order Items
    for item, price in order["items"]:
        item_row = tk.Frame(order_frame, bg="white")
        item_row.pack(fill="x", padx=10, pady=2)

        tk.Label(item_row, text=f"{item}  -  ", font=("Arial", 10), bg="white", anchor="w").pack(side="left")
        tk.Label(item_row, text=price, font=("Arial", 10), bg="white", anchor="e").pack(side="right")

    # Total Row
    total_row = tk.Frame(order_frame, bg="white")
    total_row.pack(fill="x", padx=10, pady=8)

    tk.Label(total_row, text="Total:", font=("Arial", 10, "bold"), bg="white", anchor="w").pack(side="left")
    tk.Label(total_row, text=order["total"], font=("Arial", 10, "bold"), fg="black", bg="white", anchor="e").pack(side="right")

# ---------------- Run Application ----------------
root.mainloop()
