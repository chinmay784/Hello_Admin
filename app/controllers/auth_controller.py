from app.services.auth_service import register_user, login_user

def register_controller(data):
    return register_user(data)

def login_controller(data):
    return login_user(data)