from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.permissions import IsAdminRole
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from event.api_endpoints.category.serializer import CategorySerializer
from event.models import Category


class CategoriyListAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(responses={200: CategorySerializer}, tags=['category'])
    def get(self, request):
        category = Category.objects.all()
        serialzer = CategorySerializer(category, many=True)
        return Response(serialzer.data)
    