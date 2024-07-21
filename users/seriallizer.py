from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'full_name', 'reviews', 'is_student', 'student_id', 'course_of_study',
            'institution', 'branch', 'title', 'phone_number', 'nationality', 'last_login',
            'address', 'profile_picture', 'is_paid_membership', 'is_paid_conference',
            'gender', 'college', 'date_registered',
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'is_active', 'is_staff', 'profile']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'is_active', 'is_staff', 'profile'
        ]


class MyTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to the token from the User model
        token['email'] = user.email
        token['username'] = user.username
        token['is_active'] = user.is_active
        token['is_staff'] = user.is_staff

        # Add custom claims to the token from the Profile model
        if hasattr(user, 'profile'):
            token['full_name'] = user.profile.full_name
            token['is_student'] = user.profile.is_student
            token['institution'] = user.profile.institution
            token['branch'] = user.profile.branch
            token['title'] = user.profile.title
            token['phone_number'] = user.profile.phone_number
            token['nationality'] = user.profile.nationality
            token['address'] = user.profile.address
            token['profile_picture'] = user.profile.profile_picture.url if user.profile.profile_picture else None
            token['is_paid_membership'] = user.profile.is_paid_membership
            token['is_paid_conference'] = user.profile.is_paid_conference
            token['student_id'] = user.profile.student_id
            token['gender'] = user.profile.gender
            token['course_of_study'] = user.profile.course_of_study
            token['college'] = user.profile.college
            token['date_registered'] = user.profile.date_registered.isoformat(
            ) if user.profile.date_registered else None
            token['last_login'] = user.profile.last_login.isoformat(
            ) if user.profile.last_login else None

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password', 'password2',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields do not match"}
            )
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {"email": "A user with this email already exists."}
            )
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError(
                {"username": "A user with this username already exists."}
            )
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Update User
class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()  # Nested serializer for the Profile model

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'is_active', 'is_staff', 'profile'
        ]

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        # Update User instance
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()

        # Update Profile instance
        profile.full_name = profile_data.get('full_name', profile.full_name)
        profile.reviews = profile_data.get('reviews', profile.reviews)
        profile.is_student = profile_data.get('is_student', profile.is_student)
        profile.student_id = profile_data.get('student_id', profile.student_id)
        profile.course_of_study = profile_data.get(
            'course_of_study', profile.course_of_study)
        profile.institution = profile_data.get(
            'institution', profile.institution)
        profile.branch = profile_data.get('branch', profile.branch)
        profile.title = profile_data.get('title', profile.title)
        profile.phone_number = profile_data.get(
            'phone_number', profile.phone_number)
        profile.nationality = profile_data.get(
            'nationality', profile.nationality)
        profile.address = profile_data.get('address', profile.address)
        if profile_data.get('profile_picture') is not None:
            profile.profile_picture = profile_data.get('profile_picture')
        profile.is_paid_membership = profile_data.get(
            'is_paid_membership', profile.is_paid_membership)
        profile.is_paid_conference = profile_data.get(
            'is_paid_conference', profile.is_paid_conference)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.college = profile_data.get('college', profile.college)
        profile.save()

        return instance


# Admin User Management
class AdminUserManagementSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'is_active', 'is_staff', 'profile'
        ]

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        # Update User instance
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()

        # Update Profile instance
        profile.full_name = profile_data.get('full_name', profile.full_name)
        profile.reviews = profile_data.get('reviews', profile.reviews)
        profile.is_student = profile_data.get('is_student', profile.is_student)
        profile.student_id = profile_data.get('student_id', profile.student_id)
        profile.course_of_study = profile_data.get(
            'course_of_study', profile.course_of_study)
        profile.institution = profile_data.get(
            'institution', profile.institution)
        profile.branch = profile_data.get('branch', profile.branch)
        profile.title = profile_data.get('title', profile.title)
        profile.phone_number = profile_data.get(
            'phone_number', profile.phone_number)
        profile.nationality = profile_data.get(
            'nationality', profile.nationality)
        profile.address = profile_data.get('address', profile.address)
        if profile_data.get('profile_picture') is not None:
            profile.profile_picture = profile_data.get('profile_picture')
        profile.is_paid_membership = profile_data.get(
            'is_paid_membership', profile.is_paid_membership)
        profile.is_paid_conference = profile_data.get(
            'is_paid_conference', profile.is_paid_conference)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.college = profile_data.get('college', profile.college)
        profile.save()

        return instance

    def delete(self, instance):
        instance.delete()
        return {"message": "User deleted successfully"}
