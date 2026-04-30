from django.urls import path
from account.api_endpoints.auth import LoginAPIView
from account.api_endpoints.send_email import UserRegisterCreateAPIView



urlpatterns = [
    path('register/', UserRegisterCreateAPIView.as_view(), name='register-user'),

    path('login/', LoginAPIView.as_view(), name='login'),
]

