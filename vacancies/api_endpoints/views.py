from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_yasg import openapi

from account.permissions import IsAdminUserRole
from vacancies.models import Vacancy, Skill, Requirement
from vacancies.api_endpoints.serializers import VacansySerializer, SkillSerializer, RequirementSerializer


class SkillLIstAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(responses={200: SkillSerializer}, tags=['skill'])
    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data)
    

class SkillAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=SkillSerializer, tags=['skill'])
    def post(self, request):
        serializer = SkillSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class SkillDetailAPIView(APIView):
    permission_classes = [IsAdminUserRole]

    @swagger_auto_schema(tags=['skill'])
    def delete(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        
        skill.delete()
        
        return Response(
            {"detail": "Ko'nikma muvaffaqiyatli o'chirildi."}, 
            status=status.HTTP_204_NO_CONTENT
        )
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------#

class RequirementListAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(responses={200: RequirementSerializer}, tags=['required'])
    def get(self, request):
        required = Requirement.objects.all()
        serializer = RequirementSerializer(required, many=True)
        return Response(serializer.data)
    


class RequirementAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RequirementSerializer, tags=['required'])
    def post(self, request):
        serializer = RequirementSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class RequirementDetailAPIView(APIView):
    permission_classes = [IsAdminUserRole]

    @swagger_auto_schema(tags=['required'])
    def delete(self, request, pk):
        required = get_object_or_404(Requirement, pk=pk)
        
        required.delete()
        
        return Response(
            {"detail": "Talab o'chirildi."}, 
            status=status.HTTP_204_NO_CONTENT
        )
    

#----------------------------------------------------------------------------------------------------------------------------------------#


class VacansyListAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(responses={200: VacansySerializer}, tags=['vacansy'])
    def get(self, request):
        vacansy = Vacancy.objects.filter(is_active=True)

        serializer = VacansySerializer(vacansy, many=True)
        return Response(serializer.data)
    

class VacansyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: VacansySerializer}, tags=['vacansy'])
    def get(self, request):
        vacansy = Vacancy.objects.filter(author=request.user)
        serializer = VacansySerializer(vacansy, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(request_body=VacansySerializer, tags=['vacansy'])
    def post(self, request):
        serializer = VacansySerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class VacansyDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Vacancy.objects.get(pk=pk, author=user)
        except Vacancy.DoesNotExist:
            return None

    @swagger_auto_schema(responses={200: VacansySerializer}, tags=['vacansy'])
    def get(self, request, pk):
        vacancy = self.get_object(pk, request.user)
        if not vacancy:
            return Response({"error": "Vakansiya topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VacansySerializer(vacancy)
        return Response(serializer.data)


    @swagger_auto_schema(request_body=VacansySerializer, tags=['vacansy'])
    def put(self, request, pk):
        vacancy = self.get_object(pk, request.user)
        if not vacancy:
            return Response({"error": "Vakansiya topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VacansySerializer(vacancy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT,properties=
            {
                'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='true yoki false')
            }
        ),
    tags=['vacansy'])
    def patch(self, request, pk):
        vacancy = self.get_object(pk, request.user)
        if not vacancy:
            return Response({"error": "Vakansiya topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        is_active = request.data.get('is_active')
        if is_active is not None:
            vacancy.is_active = is_active
            vacancy.save()
            status_text = "muzlatildi" if not is_active else "faollashtirildi"
            return Response({"message": f"Vakansiya muvaffaqiyatli {status_text}"})
        
        return Response({"error": "is_active maydoni yuborilmadi"}, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(operation_description="Vakansiyani bazadan butunlay o'chirish", tags=['vacansy'])
    def delete(self, request, pk):
        vacancy = self.get_object(pk, request.user)
        if not vacancy:
            return Response({"error": "Vakansiya topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        vacancy.delete()
        return Response({"message": "Vakansiya bazadan butunlay o'chirildi"}, status=status.HTTP_204_NO_CONTENT)