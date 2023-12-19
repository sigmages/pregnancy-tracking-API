from application.views.user_views import UserViewSet
from django.urls import path

urlpatterns = [
    path(
        "users",
        UserViewSet.as_view({"post": "update_or_create", "put": "update_or_create"}),
    ),
]
