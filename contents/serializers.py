from rest_framework import serializers
from courses.serializers import CourseSerializer
from .models import Content


class ContentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Content
        fields = ['id', 'name', 'content', 'video_url'] 
        read_only_fields = ['id', 'course']
        depth = 2
