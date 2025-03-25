import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Function to Handle Signup (No Database)
def register_user():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not first_name or not last_name or not email or not password:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    messagebox.showinfo("Registration Success", "User registered successfully!\n(Backend functionality will be added later)")

# Toggle Password Visibility
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        toggle_btn.configure(text="👁")
    else:
        password_entry.configure(show="*")
        toggle_btn.configure(text="🔒")

# ---------------- Main Application Window ----------------
ctk.set_appearance_mode("light")  # Options: "dark", "light", "system"
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("SuperMarket - Sign Up")
root.geometry("800x500")
root.resizable(False, False)

# ---------------- Main Frame ----------------
main_frame = ctk.CTkFrame(root, fg_color="white", corner_radius=10)
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=750, height=420)

# ---------------- Left Side - Image ----------------
left_frame = ctk.CTkFrame(main_frame, fg_color="white", width=350, height=420, corner_radius=10)
left_frame.pack(side="left", fill="both", padx=10, pady=10)

# Load and display an image
image_path = "signup.png"  # Replace with your image file
try:
    img = ctk.CTkImage(light_image=Image.open(image_path), size=(300, 300))
    image_label = ctk.CTkLabel(left_frame, image=img, text="")
    image_label.pack(pady=20)
except:
    ctk.CTkLabel(left_frame, text="🛍 Sign Up Now!", font=("Arial", 20, "bold"), text_color="#2563eb").pack(pady=80)

# ---------------- Right Side - Signup Form ----------------
right_frame = ctk.CTkFrame(main_frame, fg_color="white", width=350, height=420, corner_radius=10)
right_frame.pack(side="right", fill="both", padx=10, pady=10)

ctk.CTkLabel(right_frame, text="Create an Account", font=("Arial", 18, "bold")).pack(pady=(20, 5))

# --- First Name Entry ---
ctk.CTkLabel(right_frame, text="First Name", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
first_name_entry = ctk.CTkEntry(right_frame, font=("Arial", 12), height=35)
first_name_entry.pack(fill="x", pady=5)

# --- Last Name Entry ---
ctk.CTkLabel(right_frame, text="Last Name", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
last_name_entry = ctk.CTkEntry(right_frame, font=("Arial", 12), height=35)
last_name_entry.pack(fill="x", pady=5)

# --- Email Entry ---
ctk.CTkLabel(right_frame, text="Email", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
email_entry = ctk.CTkEntry(right_frame, font=("Arial", 12), height=35)
email_entry.pack(fill="x", pady=5)

# --- Password Entry with Toggle --- 
ctk.CTkLabel(right_frame, text="Password", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
password_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
password_frame.pack(fill="x", pady=5)

password_entry = ctk.CTkEntry(password_frame, font=("Arial", 12), height=35, show="*")
password_entry.pack(side="left", fill="x", expand=True)

toggle_btn = ctk.CTkButton(password_frame, text="🔒", width=30, height=30, command=toggle_password, fg_color="gray")
toggle_btn.pack(side="right", padx=5)

# --- Register Button ---
register_btn = ctk.CTkButton(right_frame, text="Sign Up", font=("Arial", 13, "bold"), fg_color="#2563eb",
                              height=40, corner_radius=5, command=register_user)
register_btn.pack(fill="x", pady=(15, 10))

# ---------------- Run Application ----------------
root.mainloop()
