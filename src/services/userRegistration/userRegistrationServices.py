from services.utils import generate_token, decrypt_data, encrypt_data
from services.userRegistration.userRegistrationRepository import register_user, validate_user
from werkzeug.security import generate_password_hash, check_password_hash

# Hash the password before storing it
def hash_password(password):
    try:
        return generate_password_hash(password)
    except Exception as e:
        raise Exception(f"Error hashing password: {str(e)}")

# Validate the password during login
def validate_password(stored_password, provided_password):
    try:
        return check_password_hash(stored_password, provided_password)
    except Exception as e:
        raise Exception(f"Error validating password: {str(e)}")

# Register user logic (with bcrypt password hashing)
def register_user_service(first_name, last_name, email, password):
    try:
        # Encrypt the password before storing it
        encrypted_password = encrypt_data(password)
        # Call repository to insert the user with encrypted password
        register_user(first_name, last_name, email, encrypted_password)
    except Exception as e:
        raise Exception(f"Error during user registration: {str(e)}")

# Login user logic (using bcrypt to validate password)
def login_user_service(email, password):
    try:
        user = validate_user(email)

        if user:
            stored_password = user[4]  # Assuming password is in index 4
            decrypted_password = decrypt_data(stored_password)

            # If password matches, generate JWT token
            if decrypted_password == password:
                token = generate_token(user[0])  # user[0] is user_id
                return token
            else:
                return None
        else:
            return None
    except Exception as e:
        raise Exception(f"Error during user login: {str(e)}")

