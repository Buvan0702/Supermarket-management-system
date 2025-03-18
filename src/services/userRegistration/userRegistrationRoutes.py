from services.userRegistration.userRegistrationController import register_user_controller, login_user_controller, delete_user_controller

# Registration Route (function-based)
def register_route(request_data):
    try:
        # Extracting the registration data from the provided request_data
        first_name = request_data.get('first_name')
        last_name = request_data.get('last_name')
        email = request_data.get('email')
        password = request_data.get('password')

        # Ensure all fields are present
        if not all([first_name, last_name, email, password]):
            return {"message": "All fields are required."}, 400

        # Call the controller to register the user
        register_user_controller(first_name, last_name, email, password)

        return {"message": "User registered successfully!"}, 200
    except Exception as e:
        return {"message": f"Error: {str(e)}"}, 500


# Login Route (function-based)
def login_route(request_data):
    try:
        # Extracting the login data from the provided request_data
        email = request_data.get('email')
        password = request_data.get('password')

        # Ensure both email and password are provided
        if not email or not password:
            return {"message": "Email and password are required."}, 400

        # Call the controller to attempt user login
        response = login_user_controller(email, password)
        if "token" in response:
            return {"message": "Login successful", "token": response["token"]}, 200
        else:
            return {"message": "Invalid email or password!"}, 401
    except Exception as e:
        return {"message": f"Error: {str(e)}"}, 500


# Delete User Route (function-based)
def delete_user_route(request_data):
    try:
        # Extract user ID from the request data
        user_id = request_data.get('user_id')

        # Ensure user ID is provided
        if not user_id:
            return {"message": "User ID is required."}, 400

        # Call the controller to delete the user
        delete_user_controller(user_id)

        return {"message": "User deleted successfully!"}, 200
    except Exception as e:
        return {"message": f"Error: {str(e)}"}, 500
