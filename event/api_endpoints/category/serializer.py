from rest_framework import serializers
from event.models import Category, SubCategory

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True, read_only=True)
    courses_count = serializers.IntegerField(source='courses.count', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'subcategories', 'courses_count']


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'owner', 'category', 'category_name']


