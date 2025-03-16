import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ---------------- Main Application Window ----------------
root = tk.Tk()
root.title("SuperMarket - Sign Up")
root.geometry("700x690")  # Adjusted height for proper spacing
root.resizable(False, False)  # Prevent resizing
root.configure(bg="#f2f2f2")  # Light gray background

# ---------------- Main Frame (Holds Everything) ----------------
main_frame = tk.Frame(root, bg="white", relief="flat", bd=0, highlightthickness=0)
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=650, height=600)

# ---------------- Left Side - Sign-Up Form ----------------
left_frame = tk.Frame(main_frame, bg="white", width=325, height=600)
left_frame.pack(side="left", fill="both", padx=30, pady=30)

# SuperMarket Title
tk.Label(left_frame, text="SuperMarket", font=("Arial", 20, "bold"), fg="#2563eb", bg="white").pack(anchor="w")
tk.Label(left_frame, text="Manage your shopping experience seamlessly.", 
         font=("Arial", 10), bg="white", fg="gray").pack(anchor="w", pady=5)

# Form Title
tk.Label(left_frame, text="Create your account", font=("Arial", 11, "bold"), bg="white").pack(anchor="w", pady=(20, 0))
tk.Label(left_frame, text="Fill in the details below to sign up.", font=("Arial", 9), bg="white", fg="gray").pack(anchor="w")

# Common Entry Box Style
entry_style = {"font": ("Arial", 12), "bg": "white", "relief": "solid", "bd": 1}

# --- First Name Entry ---
tk.Label(left_frame, text="First Name", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(12, 0))
first_name_entry = tk.Entry(left_frame, **entry_style)
first_name_entry.pack(fill="x", ipady=6, pady=2)

# --- Last Name Entry ---
tk.Label(left_frame, text="Last Name", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(8, 0))
last_name_entry = tk.Entry(left_frame, **entry_style)
last_name_entry.pack(fill="x", ipady=6, pady=2)

# --- Email (Gmail) Entry ---
tk.Label(left_frame, text="Gmail", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(8, 0))
email_entry = tk.Entry(left_frame, **entry_style)
email_entry.pack(fill="x", ipady=6, pady=2)

# --- Password Entry ---
tk.Label(left_frame, text="Password", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(8, 0))
password_entry = tk.Entry(left_frame, show="*", **entry_style)
password_entry.pack(fill="x", ipady=6, pady=2)

# --- Sign Up Button ---
signup_btn = tk.Button(left_frame, text="Sign Up", font=("Arial", 12, "bold"), bg="#2563eb", fg="white",
                        relief="flat", cursor="hand2", height=2, activebackground="#1d4ed8")
signup_btn.pack(fill="x", pady=(15, 10))

# --- Already have an account? Login Link ---
bottom_frame = tk.Frame(left_frame, bg="white")
bottom_frame.pack(fill="x", pady=(5, 5))

login_label = tk.Label(bottom_frame, text="Already have an account? ", font=("Arial", 9), bg="white", fg="black")
login_label.pack(side="left")

login_link = tk.Label(bottom_frame, text="Login", font=("Arial", 9, "bold"), bg="white", fg="#2563eb", cursor="hand2")
login_link.pack(side="left")

# ---------------- Right Side - Image Background ----------------
right_frame = tk.Frame(main_frame, bg="#e0ebff", width=325, height=600)
right_frame.pack(side="right", fill="both")

# Load and Display Image (Replace 'cart.png' with your actual image file)
try:
    image = Image.open("cart.png")  # Load your shopping cart image
    image = image.resize((180, 180), Image.Resampling.LANCZOS)  # Resize image
    cart_img = ImageTk.PhotoImage(image)
    img_label = tk.Label(right_frame, image=cart_img, bg="#e0ebff")
    img_label.place(relx=0.5, rely=0.5, anchor="center")
except Exception as e:
    print("Image not found. Please add 'cart.png' to the project folder.")

# ---------------- Run Application ----------------
root.mainloop()
