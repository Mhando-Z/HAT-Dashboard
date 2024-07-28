from . views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()
router.register(r'admin/users', AdminUserManagementViewSet,
                basename='adminuser')


urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('tokenRefresh/', TokenRefreshView.as_view(),
         name='token_obtain_pair'),
    path("register/", RegisterView.as_view(), name="register"),
    path("users/", getUsers, name="Users"),
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('UpdateUserProfile/', UserProfileUpdateView.as_view(),
         name='profile-update'),
    path('', include(router.urls)),
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('delete-account/', delete_account, name='delete_account'),
    path('Userprofile/change-password/',
         ChangePasswordView.as_view(), name='change-password'),
    path("CompleteRegistration/",
         UserProfileCompletionView.as_view(), name="complete"),
    #     paymentRoutes
    path('userPayment/', create_payment_intent, name='create_payment_intent'),
    path('MakePayment/', record_payment, name='makepayments_payment'),

]
