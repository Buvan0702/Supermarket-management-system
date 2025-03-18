import bcrypt
from src.services.userRegistration.userRegistrationRepository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def register_user(self, username, email, password):
        """Hash password and store user in the database"""
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return self.repository.create_user(username, email, password_hash)

    def login_user(self, email, password):
        """Verify user credentials and return authentication response"""
        user = self.repository.get_user_by_email(email)

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            return "✅ Login successful!"
        else:
            return "❌ Invalid email or password"
