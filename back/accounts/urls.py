from django.urls import path
from django.contrib.auth import views as auth_views
import accounts.views as user_views

urlpatterns = [
    path("register/", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        # user_views.MyLoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path(
        "profile/",
        user_views.profile,
        name="profile",
    ),
    path(
        "edit-profile/",
        user_views.edit_profile,
        name="edit-profile",
    ),
]
