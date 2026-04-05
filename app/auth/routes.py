from app.auth import auth

@auth.route("/login")
def login():
    return "Login Page"

@auth.route("/register")
def register():
    return "Register Page"