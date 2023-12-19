from application.views.user_views import UserViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path(
        "users",
        UserViewSet.as_view(
            {"post": "update_or_create", "put": "update_or_create"},
            name="users_update_or_create",
        ),
    ),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
