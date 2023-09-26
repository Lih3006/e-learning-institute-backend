from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'email', 'is_superuser']
        read_only_fields = ['id']
        extra_kwargs = {           
            'password': {'write_only': True},
            'username': {'validators': [UniqueValidator(queryset=Account.objects.all(),
                                                        message='A user with that username already exists.')]},
            'email': {'validators': [UniqueValidator(queryset=Account.objects.all(),
                                                        message='user with this email already exists.')]},
        }
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Account.objects.create(**validated_data)
        

class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token 