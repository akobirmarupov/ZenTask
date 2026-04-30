from django.urls import path
from account.api_endpoints.auth import LoginAPIView
from account.api_endpoints.send_email import UserRegisterCreateAPIView, UserRegisterConfirmAPIView



urlpatterns = [
    path('register/', UserRegisterCreateAPIView.as_view(), name='register-user'),
    path('register/confirm/', UserRegisterConfirmAPIView.as_view(), name='user-register-confirm'),

    path('login/', LoginAPIView.as_view(), name='login'),
]

