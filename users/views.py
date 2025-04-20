from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['role'] = self.user.role
        data['fullname'] = self.user.fullname
        return data

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

@api_view(['GET'])
def get_user_by_id(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)