from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Course
        fields = ["id", "name", "status", "start_date", "end_date", "instructor", "contents", "students_courses"]
        read_only_fields = ["contents", "students_courses"]
