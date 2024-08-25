from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # Includes all fields of the Course model

class CourseInstanceSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_code = serializers.CharField(source='course.course_code', read_only=True)
    
    class Meta:
        model = CourseInstance
        fields = ['id', 'course_title', 'course_code', 'year', 'semester']