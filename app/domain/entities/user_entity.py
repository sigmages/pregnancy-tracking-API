from domain.entities.base_entity import BaseEntity


class UserEntity(BaseEntity):
    def __init__(
        self, username, email, password, first_name, last_name, is_active=True
    ):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
        }

    @classmethod
    def from_dict(cls, payload):
        return cls(
            username=payload["username"],
            email=payload["email"],
            password=payload["password"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            is_active=payload["is_active"],
        )
