from application.serializers.user_serializer import UserSerializer
from domain.services.user_service import UserService
from rest_framework import status, viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    def update_or_create(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        user_entity = user_serializer.to_entity()
        user_entity, created = UserService.save_user(user_entity)

        return Response(
            data=user_serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )
