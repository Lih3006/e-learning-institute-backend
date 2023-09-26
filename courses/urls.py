from django.urls import  path
from .views import ListCreateCourseView, RetrieveUpdateDestroyCourseView

urlpatterns = [
    path("courses/", ListCreateCourseView.as_view()),
    path("courses/<uuid:pk>/", RetrieveUpdateDestroyCourseView.as_view()),
]