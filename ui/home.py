import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("SuperMarket Dashboard")
root.geometry("900x600")  # Adjusted height for proper spacing
root.resizable(False, False)  # Prevent resizing
root.configure(bg="#f2f2f2")  # Light gray background

# ---------------- Sidebar (Blue Navigation Menu) ----------------
sidebar = tk.Frame(root, bg="#2563eb", width=180, height=600)
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
tk.Label(main_content, text="Welcome to the SuperMarket", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(anchor="w")

# ---------------- Available Items Section ----------------
items_section = tk.Frame(main_content, bg="#f2f2f2")
items_section.pack(fill="x", pady=10)

tk.Label(items_section, text="Available Items", font=("Arial", 12, "bold"), bg="#f2f2f2").pack(anchor="w")

items_frame = tk.Frame(items_section, bg="#f2f2f2")
items_frame.pack(fill="x", pady=10)

# Product Details
products = [
    {"name": "Fresh Apples", "price": "$2.00", "image": "apple.png"},
    {"name": "Organic Bananas", "price": "$1.50", "image": "banana.png"},
    {"name": "Fresh Broccoli", "price": "$1.80", "image": "broccoli.png"}
]

# Displaying Items
for product in products:
    item_card = tk.Frame(items_frame, bg="white", width=200, height=220, relief="ridge", bd=1)
    item_card.pack(side="left", padx=10, pady=5)

    try:
        img = Image.open(product["image"])
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
        product_img = ImageTk.PhotoImage(img)
        img_label = tk.Label(item_card, image=product_img, bg="white")
        img_label.image = product_img  # Keep reference
        img_label.pack(pady=5)
    except:
        tk.Label(item_card, text="[Image]", font=("Arial", 12), bg="white").pack(pady=5)

    tk.Label(item_card, text=product["name"], font=("Arial", 10, "bold"), bg="white").pack()
    tk.Label(item_card, text=product["price"], font=("Arial", 10), fg="gray", bg="white").pack()

    add_cart_btn = tk.Button(item_card, text="Add to Cart", font=("Arial", 10, "bold"), bg="#2563eb", fg="white",
                             relief="flat", cursor="hand2", width=12, activebackground="#1d4ed8")
    add_cart_btn.pack(pady=10)

# ---------------- Checkout Section ----------------
checkout_section = tk.Frame(main_content, bg="#f2f2f2")
checkout_section.pack(fill="x", pady=10)

tk.Label(checkout_section, text="Checkout", font=("Arial", 12, "bold"), bg="#f2f2f2").pack(anchor="w")

checkout_btn = tk.Button(checkout_section, text="Proceed to Checkout", font=("Arial", 12, "bold"), bg="#16a34a", fg="white",
                         relief="flat", cursor="hand2", width=20, activebackground="#15803d")
checkout_btn.pack(pady=10)

# ---------------- Previous Orders Section ----------------
orders_section = tk.Frame(main_content, bg="#f2f2f2")
orders_section.pack(fill="x", pady=10)

tk.Label(orders_section, text="Previous Orders", font=("Arial", 12, "bold"), bg="#f2f2f2").pack(anchor="w")

orders_frame = tk.Frame(orders_section, bg="white", relief="ridge", bd=1)
orders_frame.pack(fill="x", pady=5)

orders = [
    {"name": "Order #1", "price": "$15.00"},
    {"name": "Order #2", "price": "$20.00"},
    {"name": "Order #3", "price": "$10.00"}
]

for order in orders:
    order_row = tk.Frame(orders_frame, bg="white")
    order_row.pack(fill="x", padx=10, pady=5)

    tk.Label(order_row, text=order["name"], font=("Arial", 10), bg="white", anchor="w").pack(side="left")
    tk.Label(order_row, text=order["price"], font=("Arial", 10, "bold"), bg="white", anchor="e").pack(side="right")

# ---------------- Run Application ----------------
root.mainloop()
