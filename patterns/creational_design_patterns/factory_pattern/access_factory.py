from const import User
from access_control import AdminAccessControl, SupervisorAccessControl, UserAccessControl

class AccessControlFactory:
    _role_mapping = {
        User.ADMIN: AdminAccessControl,
        User.SUPERVISOR: SupervisorAccessControl,
        User.USER: UserAccessControl
    }

    def __init__(self, user_type: User):
        self.user_type = user_type

    def get_permissions(self):
        if self.user_type in self._role_mapping:
            accessControl = self._role_mapping[self.user_type]
            return accessControl().get_permissions()
        else:
            # note
            raise ValueError(f"Invalid user type: {self.user_type}")

