import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

# --- Username Entry ---
tk.Label(left_frame, text="Username", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(15, 0))
username_entry = tk.Entry(left_frame, font=("Arial", 12), bg="white", relief="solid", bd=1)
username_entry.pack(fill="x", ipady=5, pady=2)

# --- Password Entry ---
tk.Label(left_frame, text="Password", font=("Arial", 10, "bold"), bg="white").pack(anchor="w", pady=(10, 0))
password_entry = tk.Entry(left_frame, show="*", font=("Arial", 12), bg="white", relief="solid", bd=1)
password_entry.pack(fill="x", ipady=5, pady=2)

# --- Login Button ---
login_btn = tk.Button(left_frame, text="Login", font=("Arial", 12, "bold"), bg="#2563eb", fg="white",
                       relief="flat", cursor="hand2", height=2, activebackground="#1d4ed8")
login_btn.pack(fill="x", pady=(15, 10))

# --- Sign Up & Forgot Password Links ---
bottom_frame = tk.Frame(left_frame, bg="white")
bottom_frame.pack(fill="x", pady=10)  # Adjusted padding to prevent cutoff

signup_label = tk.Label(bottom_frame, text="Already have an account? Sign Up", font=("Arial", 9), 
                        bg="white", fg="#2563eb", cursor="hand2")
signup_label.pack()

forgot_label = tk.Label(bottom_frame, text="Forgot Password?", font=("Arial", 9), bg="white", fg="#2563eb", cursor="hand2")
forgot_label.pack(pady=(5, 0))

# ---------------- Right Side - Image Background ----------------
right_frame = tk.Frame(main_frame, bg="#e0ebff", width=350, height=420)
right_frame.pack(side="right", fill="both")

# Load and Display Image (Replace 'cart.png' with your actual image file)
try:
    image = Image.open("cart.png")  # Load your shopping cart image
    image = image.resize((150, 150), Image.Resampling.LANCZOS)  # Resize image
    cart_img = ImageTk.PhotoImage(image)
    img_label = tk.Label(right_frame, image=cart_img, bg="#e0ebff")
    img_label.place(relx=0.5, rely=0.5, anchor="center")
except Exception as e:
    print("Image not found. Please add 'cart.png' to the project folder.")

# ---------------- Run Application ----------------
root.mainloop()
