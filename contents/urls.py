from django.urls import path
from .views import ListCreateContentView, RetrieveUpdateDestroyContentView


urlpatterns = [
    path("courses/<uuid:course_id>/contents/", ListCreateContentView.as_view()),
    path("courses/<uuid:course_id>/contents/<uuid:pk>/", RetrieveUpdateDestroyContentView.as_view()),    
]
