from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.generics import GenericAPIView
from django.urls import reverse
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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework_simplejwt.tokens import TokenError, AccessToken
from django.shortcuts import render, redirect
from .models import *
from . seriallizer import *
import uuid
import stripe


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # changed from true to false
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Create the response data
        response_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }

        # Create the response
        response = Response(response_data, status=status.HTTP_201_CREATED)
        response['x-auth-token'] = access_token
        response['access-control-expose-headers'] = 'x-auth-token'

        return response

    def perform_create(self, serializer):
        return serializer.save()


# Getting users
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


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


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    user = request.user
    user.delete()
    return Response({"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# channge password view
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Password changed successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# userupdate view


class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    # Supports JSON, Multipart, and Form-encoded data
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    # parser_classes = [MultiPartParser, FormParser]  # Add this line

    def get_object(self):
        # Return the current user object
        return self.request.user

    def patch(self, request, *args, **kwargs):
        # Use PATCH method to support partial updates
        return super().patch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Handle PUT request for complete updates
        return super().put(request, *args, **kwargs)

# Stripe payment integration
# views.py


stripe.api_key = set
stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = data['amount']

            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd'
            )
            return JsonResponse({
                'clientSecret': payment_intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@api_view(['POST'])
def record_payment(request):
    user = request.user
    amount = request.data.get('amount')
    transaction_id = str(uuid.uuid4())  # Generate a unique transaction ID
    status = 'success'  # Assume success for simplicity

    payment = Payment.objects.create(
        user=user, amount=amount, transaction_id=transaction_id, status=status)
    serializer = PaymentSerializer(payment)

    # Generate receipt (you can customize the receipt details)
    receipt = {
        'user': user.username,
        'amount': amount,
        'transaction_id': transaction_id,
        'date': payment.date,
    }

    return Response({'payment': serializer.data, 'receipt': receipt}, status=status.HTTP_201_CREATED)


class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = User.objects.get(id=user_id)

            if user.is_active:
                # Render already verified template
                login_url = "https://historical-association-of-tanzania.vercel.app/Login/"

                return render(request, 'hattz/already_verified.html', {
                    'username': user.username,
                    'login_url': login_url
                })

            # Activate the user
            user.is_active = True
            user.save()

            # Render success template
            # Replace with your actual frontend login URL
            login_url = "https://historical-association-of-tanzania.vercel.app/Login/"
            return render(request, 'hattz/email_verification_success.html', {'username': user.username, 'login_url': login_url})

        except TokenError:
            return Response({"message": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()


class ResendEmailVerification(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            # Get user by email
            user = User.objects.get(email=email)

            # Check if the user is already active
            if user.is_active:
                return Response({
                    'detail': 'Your account is already verified.',
                    'code': 'user_already_verified'
                }, status=status.HTTP_400_BAD_REQUEST)

            # Call the function to send verification email
            self.send_verification_email(user, request)

            return Response({'detail': 'Verification email resent'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({
                'detail': 'User with this email does not exist',
                'code': 'user_not_found'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'detail': 'An error occurred while processing your request',
                'code': 'server_error'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def send_verification_email(self, user, request):
        # Generate a new token for the user
        token = RefreshToken.for_user(user).access_token

        # Generate verification link
        verification_link = reverse(
            'email-verify', kwargs={'token': str(token)})
        absurl = request.build_absolute_uri(verification_link)

        # Render the HTML template for the email
        html_message = render_to_string('hattz/email_verification.html', {
            'username': user.username,
            'verification_link': absurl,
        })

        # Create a plain text version of the email
        plain_message = strip_tags(html_message)

        # Send email
        send_mail(
            subject='Verify your email address',
            message=plain_message,
            from_email='from@example.com',  # Update with your sender email
            recipient_list=[user.email],
            fail_silently=False,
            html_message=html_message,  # HTML version of the email
        )
