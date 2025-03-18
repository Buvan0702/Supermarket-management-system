from src.entities.profileDetails.repository import ProfileRepository

class ProfileService:
    def __init__(self):
        self.repository = ProfileRepository()

    def get_profile(self, user_id):
        """Retrieve user profile details"""
        profile = self.repository.get_profile_by_user_id(user_id)
        if profile:
            return profile
        else:
            return "❌ Profile not found"

    def update_profile(self, user_id, username, email):
        """Update user profile details"""
        return self.repository.update_profile(user_id, username, email)
