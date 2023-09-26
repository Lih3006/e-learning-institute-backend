from django.db import models
from accounts.models import Account
from uuid import uuid4


class StatusCourse(models.TextChoices):
    in_progress = 'in progress',
    finished = 'finished',
    DEFAULT = 'not started',
    
    
class Course(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=11, choices=StatusCourse.choices, default=StatusCourse.DEFAULT)
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='courses', null=True, default=None)
    students = models.ManyToManyField(Account, through='students_courses.StudentCourse', related_name='my_courses')
    

