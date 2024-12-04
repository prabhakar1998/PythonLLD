from access_factory import AccessControlFactory

def test_user_permissions(user_type):
    access_control = AccessControlFactory(user_type)
    permissions = access_control.get_permissions()
    print(f"Allowed permissions for the {user_type} are: ", permissions)


if __name__ == "__main__":
    user_type = "admin"
    test_user_permissions("admin")
    test_user_permissions("supervisor")
    test_user_permissions("user")