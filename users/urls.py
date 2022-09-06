from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import CustomTokenObtainPairView, VerifyUser
from users.views import Register

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('register/', Register.as_view(), name='register'),
    path('check-for-admin/', VerifyUser.as_view(), name='check-for-admin')
]
