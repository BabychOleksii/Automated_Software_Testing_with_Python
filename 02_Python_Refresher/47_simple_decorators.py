user = {"username": "Jose", "access_level": "guest"}


def get_admin_password():
    return "admin_1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


try_to_get_admin_password = make_secure(get_admin_password)


print(try_to_get_admin_password())
