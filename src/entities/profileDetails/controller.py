from src.entities.profileDetails.services import ProfileService

class ProfileController:
    def __init__(self):
        self.profile_service = ProfileService()

    def view_profile(self, user_id):
        """Fetch the profile details of a user."""
        return self.profile_service.get_profile(user_id)

    def update_profile(self, user_id, username, email):
        """Update the profile details of a user."""
        return self.profile_service.update_profile(user_id, username, email)

# Example usage:
# if __name__ == "__main__":
#     controller = ProfileController()
#     print(controller.view_profile(1))  # View profile of user with ID 1
#     print(controller.update_profile(1, "new_username", "new_email@example.com"))  # Update profile of user
