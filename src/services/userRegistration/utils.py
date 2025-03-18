import jwt
import os
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

# Secret key for signing JWT tokens (You should store this securely in the .env file)
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

# Encryption key for securing sensitive data (like passwords)
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "your_encryption_key")

# Generate JWT token for the user
def generate_token(user_id):
    """
    Generate a JWT token with a user ID and expiration time.
    """
    try:
        expiration_time = datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
        token = jwt.encode({
            "user_id": user_id,
            "exp": expiration_time
        }, SECRET_KEY, algorithm="HS256")
        return token
    except Exception as e:
        raise Exception(f"Error generating JWT token: {str(e)}")

# Verify the JWT token (check validity and expiration)
def verify_token(token):
    """
    Verifies the JWT token. Returns the decoded payload if valid, else raises error.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired.")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token.")
    except Exception as e:
        raise Exception(f"Error verifying token: {str(e)}")

# Decode the JWT token (retrieve the payload)
def decode_token(token):
    """
    Decode the JWT token and return the payload.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except Exception as e:
        raise Exception(f"Error decoding token: {str(e)}")

# Encrypt data (e.g., password) using the encryption key
def encrypt_data(data):
    """
    Encrypt sensitive data (like password) before storing.
    """
    try:
        f = Fernet(ENCRYPTION_KEY)
        encrypted_data = f.encrypt(data.encode())  # Encrypt the data
        return encrypted_data
    except Exception as e:
        raise Exception(f"Error encrypting data: {str(e)}")

# Decrypt the encrypted data
def decrypt_data(encrypted_data):
    """
    Decrypt the sensitive data (like password) for verification.
    """
    try:
        f = Fernet(ENCRYPTION_KEY)
        decrypted_data = f.decrypt(encrypted_data).decode()  # Decrypt the data
        return decrypted_data
    except Exception as e:
        raise Exception(f"Error decrypting data: {str(e)}")
