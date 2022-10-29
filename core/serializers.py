from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as CurrentUser
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields=['id','username','password','email','first_name','last_name']
class UserSerializer(CurrentUser):
    class Meta(CurrentUser.Meta):
        fields = ['id','username','email', 'first_name', 'last_name']

