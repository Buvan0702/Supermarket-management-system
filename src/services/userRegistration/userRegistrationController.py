from services.userRegistration.userRegistrationRepository import register_user, login_user

def handle_registration(username, email, password):
    return register_user(username, email, password)

def handle_login(email, password):
    return login_user(email, password)
