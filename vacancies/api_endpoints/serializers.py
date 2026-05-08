from rest_framework import serializers

from vacancies.models import Vacancy, Skill, Requirement


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'vacancy', 'text']


class VacansySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    requirements = RequirementSerializer(many=True, read_only=True)
    
    skill_names = serializers.ListField(
        child=serializers.CharField(), 
        write_only=True, 
        required=False
    )
    requirement_texts = serializers.ListField(
        child=serializers.CharField(), 
        write_only=True, 
        required=False
    )

    class Meta:
        model = Vacancy
        fields = [
            'id', 'title', 'company_name', 'location', 'job_type', 
            'salary_range', 'description', 'status', 'is_active',
            'skills', 'requirements', 'skill_names', 'requirement_texts', 'created_at'
        ]
        read_only_fields = ['status', 'is_active', 'created_at']

    def create(self, validated_data):
        # Pop qilishda aniq e'lon qilingan nomdan foydalanamiz
        skill_names = validated_data.pop('skill_names', [])
        requirement_texts = validated_data.pop('requirement_texts', [])
        
        vacancy = Vacancy.objects.create(**validated_data)

        # Skilllarni qo'shish
        for name in skill_names:
            skill, _ = Skill.objects.get_or_create(name=name)
            vacancy.skills.add(skill)

        # Requirementlarni qo'shish
        for text in requirement_texts:
            Requirement.objects.create(vacancy=vacancy, text=text)

        return vacancy