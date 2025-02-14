from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    UserCreateView,
    email_verification,
    UserListView,
    UserUpdateView,
    UserDetailView,
    UserProfileUpdateView,
)

app_name = UsersConfig.name


urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("list/", UserListView.as_view(), name="user_list"),
    path("detail/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path(
        "profile/",
        UserProfileUpdateView.as_view(template_name="profile.html"),
        name="profile",
    ),
]
