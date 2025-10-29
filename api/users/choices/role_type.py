from enum import Enum

class RoleType(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

    @classmethod
    def choices(cls):
        return [(member.name, member.value) for member in cls]