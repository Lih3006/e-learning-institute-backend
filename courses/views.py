from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminOrReadOnly, IsSuperuserOrParticipant
from .models import Course
from .serializers import CourseSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema 


class ListCreateCourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    @extend_schema(
        operation_id="list_create_course",
        summary="Listar e criar cursos",
        description="Endpoint para listar e criar cursos.",        
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="create_course",
        summary="Criar curso",
        description="Endpoint para criar um novo curso.",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrParticipant]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    @extend_schema(
        operation_id="retrieve_course",
        summary="Detalhes de um curso específico",
        description="Endpoint para visualizar detalhes de um curso.",        
    )
    def get(self, request, *args, **kwargs):      
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="update_course",
        summary="Atualização de um curso específico",
        description="Endpoint para atualizar detalhes de um curso.",        
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="update_course",
        exclude=True,        
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="destroy_course",
        summary="Exclusão de um curso específico",
        description="Endpoint para excluir um curso.",        
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)