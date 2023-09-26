from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import Account
from accounts.permissions import IsAdminOrReadOnly
from courses.models import Course
from students_courses.models import StudentCourse
from students_courses.serializers import StudentCourseSerializer
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema


class ListUpdateStudentCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = StudentCourseSerializer 
    lookup_field = 'pk'
    
    @extend_schema(
        operation_id="update_student_course",
        summary="Cria relacionamento estudante ao curso",
        description="Endpoint para vincular um usuário ao perfil de estudante juntamente com um curso de interesse.",        
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="retrieve_student_course",
        summary="Detalhes de alunos vinculados a um curso específico",
        description="Endpoint para visualizar detalhes de alunos vinculados a um curso específico.",        
    )
    def get(self, request, *args, **kwargs):      
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="update_content",
        exclude=True,        
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    
class DestroyStudentCourseView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = StudentCourseSerializer 
    lookup_url_kwarg = 'student_id'
    
    @extend_schema(
        operation_id="destroy_student_course",
        summary="Exclusão de um aluno de um curso específico",
        description="Endpoint  para desvincular o relaacionamento entre estudante(usuário) e curso.",        
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def perform_destroy(self, instance):
        course_id = self.kwargs['course_id']
        pk1 = self.kwargs['student_id']         
        try:
            StudentCourse.objects.get(course_id=course_id, student_id=pk1)
        except StudentCourse.DoesNotExist:        
            raise NotFound("this id is not associated with this course.")
        return instance.delete()