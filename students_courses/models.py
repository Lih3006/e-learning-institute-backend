from django.db import models
from uuid import uuid4


class StudentCourseStatus(models.TextChoices):
    pending = 'pending'
    accepted = 'accepted'
    


class StudentCourse(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid4, editable=False)   
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='students_courses')
    student = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='students_courses')
    status = models.TextField(choices=StudentCourseStatus.choices, default=StudentCourseStatus.pending)
    
    
