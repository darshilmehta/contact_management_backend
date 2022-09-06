from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenVerifySerializer
from rest_framework import  serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password')
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'admin': self.user.is_superuser})
        data.update({'name': self.user.username})
        return data