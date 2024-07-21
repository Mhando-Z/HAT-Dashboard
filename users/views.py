from django.urls import reverse
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.generics import RetrieveAPIView
from .models import *
from . seriallizer import *


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


# Getting users
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# Updating User
class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Obtain userr profile details


class UserProfileView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# admin user management


class AdminUserManagementViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserManagementSerializer
    permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


# Password resetting


@api_view(['POST'])
def password_reset_request(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    if user:
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_link = request.build_absolute_uri(
            reverse('password_reset_confirm', kwargs={
                    'uidb64': uid, 'token': token})
        )
        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: {reset_link}',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )
    return Response({"message": "Password reset link sent."}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            new_password = request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid token or user ID."}, status=status.HTTP_400_BAD_REQUEST)
