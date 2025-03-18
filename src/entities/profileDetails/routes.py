from src.entities.profileDetails.controller import ProfileController

class ProfileRoutes:
    def __init__(self):
        self.controller = ProfileController()

    def start(self):
        while True:
            print("\n🔑 Profile Management")
            print("1️⃣ View Profile")
            print("2️⃣ Update Profile")
            print("3️⃣ Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                user_id = int(input("Enter user ID to view profile: "))
                print(self.controller.view_profile(user_id))

            elif choice == "2":
                user_id = int(input("Enter user ID to update profile: "))
                email = input("Enter new email: ")
                print(self.controller.update_profile(user_id, email))

            elif choice == "3":
                print("👋 Exiting...")
                break

            else:
                print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    ProfileRoutes().start()
