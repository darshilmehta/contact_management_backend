from rest_framework.response import Response
from .serializer import CustomUserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken
from .models import CustomUser

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class Register(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyUser(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        access_token = request.data["access_token"]
        access = AccessToken(access_token)
        user = CustomUser.objects.get(id = access['user_id'])
        content = {
            "is_super_user": user.is_superuser
        }
        return Response(content, status=status.HTTP_200_OK)