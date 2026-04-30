from account.tokens import (
    generate_email_confirm_token,
    generate_temporary_password,
    verify_email_confirm_token
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from drf_yasg.utils import swagger_auto_schema

from account.email_send import send_email
from account.api_endpoints.serializers import RegisterInputSerializer


User = get_user_model() 
    

class UserRegisterCreateAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=RegisterInputSerializer, tags=['send_sms'])
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'detail': 'Email va parol kiritilmadi.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if user and user.is_confirmed:
            return Response({
                "detail": "Bunday foydalanuvchi mavjud va tasdiqlangan. Iltimos, login qiling.",
                "is_confirmed": True
            }, status=status.HTTP_400_BAD_REQUEST)

        if user and not user.is_confirmed:
         
            now = timezone.now()
            if user.date_joined > now - timedelta(minutes=30):
                return Response({
                    "detail": "Sizga tasdiqlash linki yuborilgan. Iltimos, yarim soatdan keyin urinib ko'ring.",
                    "is_confirmed": False
                }, status=status.HTTP_429_TOO_MANY_REQUESTS)

            user.set_password(password)
            user.date_joined = now 
            user.save()
            
            token = generate_email_confirm_token(user)
            send_email(
                subject="Tasdiqlash kodi",
                intro_text="Bunday user bazada mavjud lekin tasdiqlanmagan va tasdiqlash linki yuborildi.",
                email=user.email,
                token=token,
                template="email/reset_password_email.html"
            )
            return Response({
                "detail": "Bunday user bazada mavjud lekin tasdiqlanmagan va tasdiqlash linki yuborildi.",
                "is_confirmed": False
            }, status=status.HTTP_200_OK)

        new_user = User.objects.create_user(
            email=email,
            password=password,
            is_confirmed=False
        )

        token = generate_email_confirm_token(new_user)
        send_email(
            subject="Tasdiqlash kodi",
            intro_text="Xush kelibsiz! Emailingizni tasdiqlang:",
            email=new_user.email,
            token=token,
            template="email/reset_password_email.html"
        )

        return Response({
            "detail": "Yangi foydalanuvchi yaratildi. Emailga tasdiqlash kodi yuborildi.",
            "is_confirmed": False
        }, status=status.HTTP_201_CREATED)