from django.urls import path
from .api_endpoints import views

urlpatterns = [
    path('skills/', views.SkillLIstAPIView.as_view(), name='skill-list'),
    path('skills/create/', views.SkillAPIView.as_view(), name='skill-create'), 
    path('skills/<int:pk>/delete/', views.SkillDetailAPIView.as_view(), name='skill-delete'),

    path('requirements/', views.RequirementListAPIView.as_view(), name='requirement-list'),
    path('requirements/create/', views.RequirementAPIView.as_view(), name='requirement-create'),
    path('requirements/<int:pk>/delete/', views.RequirementDetailAPIView.as_view(), name='requirement-delete'),

    path('vacancies/', views.VacansyListAPIView.as_view(), name='vacancy-list'),
    path('my-vacancies/', views.VacansyAPIView.as_view(), name='my-vacancy'),
    path('vacancies/<int:pk>/', views.VacansyDetailAPIView.as_view(), name='vacancy-detail'),
]