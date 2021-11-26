from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize Student model.
    """
    class Meta:
        model = Student
        fields = ('id', 'name', 'student_id', 'email', 'dept_choice')


class StudentRegisterationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registeration requests and create a new user.
    """
    class Meta:
        model = Student
        fields = ('id', 'name', 'student_id',
                  'email', 'dept_choice', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_name(self, value):
        """
        Check that the given student name is valid
        """
        if not len(value.split()) > 1:
            raise serializers.ValidationError("Please enter a full name")
        return value

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)


class StudentLoginSerializer(serializers.Serializer):
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
