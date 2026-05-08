from django.db import models
from django.conf import settings

from common.models import BaseModel


class Skill(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    
    JOB_TYPE_CHOICES = [
        ('full_time', "To'liq ish kuni"),
        ('part_time', "Yarim ish kuni"),
        ('remote', "Masofaviy"),
        ('internship', "Amaliyot"),
    ]

    STATUS_CHOICES = [
        ('active', 'Faol'),
        ('hidden', 'Vaqtincha toʻxtatilgan'),
        ('closed', 'Yopilgan'),
    ]

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full_time')
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    skills = models.ManyToManyField(Skill, related_name="vacancies")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.company_name}"


class Requirement(BaseModel):
    vacancy = models.ForeignKey(Vacancy, related_name="requirements", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text