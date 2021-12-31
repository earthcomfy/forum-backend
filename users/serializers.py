from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model

from .models import Student


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize User model.
    """
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'role',)


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize Student model.
    """
    student = UserSerializer()

    class Meta:
        model = Student
        fields = ('student', 'student_ID', 'dept_choice')


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize registration of Users.
    """
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'name', 'email', 'role', 'password', 'tokens',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def validate_name(self, value):
        """
        Check that the given student name is valid
        """
        if not len(value.split()) > 1:
            raise serializers.ValidationError("Please enter a full name")
        return value

    def get_tokens(self, obj):
        jwt = RefreshToken.for_user(obj)
        return {
            'refresh': str(jwt),
            'access': str(jwt.access_token)
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class StudentRegisterationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registeration requests and create a new user.
    """
    student = UserRegistrationSerializer()

    class Meta:
        model = Student
        fields = ('student', 'student_ID', 'dept_choice',)

    def create(self, validated_data):
        user_data = validated_data.pop('student')
        user_data['role'] = 'S'
        user = UserRegistrationSerializer.create(
            UserRegistrationSerializer(), validated_data=user_data)
        student = Student.objects.create(student=user, **validated_data)
        return student


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')
