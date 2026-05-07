from rest_framework import serializers
from event.models import Course, Lesson, Enrollment

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id', 'course', 'title', 'description', 
            'video_url', 'video_file', 'duration_display', 'is_preview'
        ]
        read_only_fields = ['owner']


from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    students_count = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    is_liked = serializers.SerializerMethodField()
    is_enrolled = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'name', 'description', 'category', 
            'sub_category', 'price', 'image', 'lessons', 'is_enrolled',
            'students_count', 'likes_count', 'average_rating', 'is_liked'
        ]
        read_only_fields = ['owner']

    def get_is_enrolled(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.enrollments.filter(user=request.user, status='approved').exists()
        return False

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False
        

class EnrollmentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    course_name = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'user_name', 'course', 'course_name', 'date_enrolled']
        read_only_fields = ['user'] 