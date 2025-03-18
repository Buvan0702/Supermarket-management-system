from services.userRegistration.userRegistrationServices import register_user_service, login_user_service, delete_user_service

# User Registration Controller
def register_user_controller(first_name, last_name, email, password):
    try:
        register_user_service(first_name, last_name, email, password)
    except Exception as e:
        raise Exception(f"Error in register_user_controller: {str(e)}")

# User Login Controller
def login_user_controller(email, password):
    try:
        token = login_user_service(email, password)
        if token:
            return {"message": "Login successful", "token": token}
        else:
            return {"message": "Invalid email or password!"}
    except Exception as e:
        raise Exception(f"Error in login_user_controller: {str(e)}")

# Delete User Controller
def delete_user_controller(user_id):
    try:
        delete_user_service(user_id)
    except Exception as e:
        raise Exception(f"Error in delete_user_controller: {str(e)}")
