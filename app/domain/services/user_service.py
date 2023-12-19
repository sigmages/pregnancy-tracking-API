from django.contrib.auth.models import User as UserModel
from domain.entities.user_entity import UserEntity
from domain.exceptions.database_exceptions import NotFoundError


class UserService:
    @classmethod
    def save_user(cls, user_entity):
        user_model, created = UserModel.objects.update_or_create(
            username=user_entity.username,
            defaults={
                "email": user_entity.email,
                "first_name": user_entity.first_name,
                "last_name": user_entity.last_name,
                "is_active": user_entity.is_active,
            },
        )
        user_model.set_password(user_entity.password)
        user_model.save()

        return user_entity, created

    @classmethod
    def get_user_by_username(cls, username):
        try:
            user_model = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise NotFoundError("Usuário não encontrado.")

        return UserEntity(
            username=user_model.model.username,
            email=user_model.model.email,
            password=user_model.model.password,
            first_name=user_model.model.first_name,
            last_name=user_model.model.last_name,
            is_active=user_model.model.is_active,
        )
