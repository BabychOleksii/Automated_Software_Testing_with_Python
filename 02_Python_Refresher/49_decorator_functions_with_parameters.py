import functools

user = {"username": "Jose", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password(panel):
    if panel == "administrator":
        return "admin_1234"
    elif panel == "billing":
        return "billing_5678"


print(get_admin_password("administrator"))
print(get_admin_password("billing"))
