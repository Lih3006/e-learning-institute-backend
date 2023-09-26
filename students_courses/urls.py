from django.urls import path
from .views import ListUpdateStudentCourseView, DestroyStudentCourseView


urlpatterns = [
    path("courses/<uuid:pk>/students/", ListUpdateStudentCourseView.as_view()),
    path("courses/<uuid:course_id>/students/<uuid:student_id>/", DestroyStudentCourseView.as_view()),  
]
