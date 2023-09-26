from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.models import Course
from contents.serializers import ContentSerializer
from .models import Content
from accounts.permissions import IsAdminOrReadOnly, IsSuperuserOrParticipant
from drf_spectacular.utils import extend_schema


class ListCreateContentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    
    
    @extend_schema(
        operation_id="list_content",
        summary="Listar e criar conteúdo para um curso específico",
        description="Endpoint para listar e criar conteúdo relacionado a cursos.",        
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="create_content",
        summary="Criar conteúdo para um curso específico",
        description="Endpoint para criar um novo conteúdo relacionado a cursos.",        
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        course_id = self.kwargs['course_id']
        
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise serializer.ValidationError("Course with this ID does not exist.")
        
        serializer.save(course=course)
        
        
class RetrieveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrParticipant]
    
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    
    @extend_schema(
        operation_id="retrieve_content",
        summary="Detalhes de um conteúdo específico",
        description="Endpoint para visualizar detalhes de um conteúdo.",        
    )
    def get(self, request, *args, **kwargs):      
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="partial_update_content",
        summary="Atualização de um conteúdo específico",
        description="Endpoint para atualizar detalhes de um conteúdo.",        
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="update_content",
        exclude=True,        
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="destroy_content",
        summary="Exclusão de um conteúdo específico",
        description="Endpoint excluir um conteúdo.",        
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)