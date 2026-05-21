from django.urls import path
from account.api_endpoints.test.views import (
    RegisterView,
    RegisterVerifyView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

urlpatterns = [
    # Ro'yxatdan o'tish
    path("auth/register/",        RegisterView.as_view(),       name="register"),
    path("auth/register/verify/", RegisterVerifyView.as_view(), name="register-verify"),

    # Parol tiklash
    path("auth/password/reset/",         PasswordResetRequestView.as_view(), name="password-reset"),
    path("auth/password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
]