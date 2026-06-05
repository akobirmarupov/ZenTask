from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account.api_endpoints.test.views import (
    RegisterView,
    RegisterVerifyView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    LoginView
)

urlpatterns = [
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # Ro'yxatdan o'tish
    path("auth/register/",        RegisterView.as_view(),       name="register"),
    path("auth/register/verify/", RegisterVerifyView.as_view(), name="register-verify"),

    # Parol tiklash
    path("auth/password/reset/",         PasswordResetRequestView.as_view(), name="password-reset"),
    path("auth/password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path("auth/login/", LoginView.as_view(), name="login"),

]