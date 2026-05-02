from django.urls import path
from event.api_endpoints.category.views import CategoriyListAPIView 



urlpatterns = [
    path('categpry/', CategoriyListAPIView.as_view(), name='category-get'),
]

