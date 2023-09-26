from rest_framework.generics import ListCreateAPIView
from .models import Account
from .serializers import AccountSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.serializers import CustomJWTSerializer
from drf_spectacular.utils import extend_schema


class AccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    @extend_schema(
        operation_id="account_list", 
        summary='Listagem de usuário', 
        description='Rota para listar todos os usuários da aplicacao')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="create_account",
        summary="Criar Usuário",
        description="Endpoint para criar um novo usuário.",        
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer