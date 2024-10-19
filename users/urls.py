from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

# DRF router for admin user management
router = DefaultRouter()
router.register(r'admin/users', AdminUserManagementViewSet,
                basename='adminuser')

urlpatterns = [
    # Authentication and token management
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenRefresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User registration
    path("register/", RegisterView.as_view(), name="register"),

    # User list
    path("users/", getUsers, name="Users"),

    # User profile and profile updates
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('UpdateUserProfile/', UserProfileUpdateView.as_view(),
         name='profile-update'),

    # Admin user management (via DRF ViewSet)
    path('', include(router.urls)),

    # Password reset and confirmation
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Account management
    path('delete-account/', delete_account, name='delete_account'),

    # Change password
    path('Userprofile/change-password/',
         ChangePasswordView.as_view(), name='change-password'),

    # Payment routes
    path('userPayment/', create_payment_intent, name='create_payment_intent'),
    path('MakePayment/', record_payment, name='makepayments_payment'),

    # dj-rest-auth registration and email confirmation
    # For email confirmation and resend email
    path('auth/', include('dj_rest_auth.registration.urls')),
    path('email-verify/<str:token>/',
         VerifyEmailView.as_view(), name='email-verify'),
    path('resend-email-verification/', ResendEmailVerification.as_view(),
         name='resend-email-verification'),
]
