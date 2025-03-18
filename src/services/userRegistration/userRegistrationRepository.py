import mysql.connector
from database_config import get_db_connection

def register_user(username, email, password):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Check if the email already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        print("User already exists!")
        return False

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                   (username, email, password))
    connection.commit()
    cursor.close()
    connection.close()
    print("User registered successfully!")
    return True

def login_user(email, password):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Retrieve user from the database
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if not user:
        print("User not found!")
        return False

    # Check if the provided password matches the stored password
    stored_password = user[3]  # The password is in the 4th column (index 3)
    if stored_password == password:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials!")
        return False
