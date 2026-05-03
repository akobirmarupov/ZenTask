from django.urls import path
from event.api_endpoints.category.views import (
    CategoriyListAPIView, CategoryAPIVIew, CategoryDetailAPIView, 
    SubcategoryAPIView, SubcategoryListAPIView,SubCategoryDetailAPIView)

urlpatterns = [
    path('category/', CategoriyListAPIView.as_view(), name='category-list'),
    path('dt-category/<int:pk>/', CategoryDetailAPIView.as_view(), name='dt-category'),
    path('my-categories/', CategoryAPIVIew.as_view(), name='admin-category-list'),

    path('subcategory/', SubcategoryListAPIView.as_view(), name='subcategory-list'),
    path('dt-subcategory/<int:pk>/', SubCategoryDetailAPIView.as_view(), name='dt-subcategory'),
    path('my-subcategories/', SubcategoryAPIView.as_view(), name='admin-subcategory-list'),
]