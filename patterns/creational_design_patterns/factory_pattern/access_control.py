from abc import ABC, abstractmethod
from const import USER, SUPERVISOR, ADMIN

class AccessControl(ABC):

    @abstractmethod
    def get_permissions(self):
        pass


class AdminAccessControl(AccessControl):

    def get_permissions(self):
        return ["read", "create", "update", "delete"]
    
class SupervisorAccessControl(AccessControl):

    def get_permissions(self):
        return ["read", "create", "update"]

class UserAccessControl(AccessControl):

    def get_permissions(self):
        return ["read"]
