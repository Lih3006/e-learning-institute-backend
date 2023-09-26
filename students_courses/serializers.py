from accounts.models import Account
from courses.models import Course
from .models import StudentCourse
from rest_framework import serializers
from rest_framework import serializers
from rest_framework.exceptions import ParseError


class StudentCourseRepresentationSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source='student.id', read_only=True)
    student_username = serializers.CharField(source='student.username', read_only=True)
    student_email = serializers.CharField(source='student.email', read_only=True)
    
    class Meta:
        model = StudentCourse
        fields = ['id', 'student_id', 'student_username', 'student_email', 'status']
        read_only_fields = ['id', 'student_id', 'student_username', 'student_email']


class StudentCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseRepresentationSerializer(many=True)
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'students_courses']
        read_only_fields = ["name", "students_courses"]
        depth = 2
            
    def update(self, instance: Course, validated_data):       
        request = self.context.get('request')       
        students_data = request.data.get("students_courses", [])
        for student in students_data:
            student_email = student['student_email']  
            student_status = student.get('status', None)           
            try:
                student_exists = Account.objects.get(email=student_email)
                instance.students.add(student_exists) 
                student_course, created = instance.students_courses.get_or_create(student=student_exists)
                if student_status is not None:
                    student_course.status = student_status
                    student_course.save()           
            except Account.DoesNotExist:                
                raise ParseError(f"No active accounts was found: {student_email}.")
        return instance