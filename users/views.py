from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import StudentSerializer, StudentRegisterationSerializer, StudentLoginSerializer


class StudentRegisterationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new student. 
    """
    permission_classes = (AllowAny,)
    serializer_class = StudentRegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {
            'refresh': str(token),
            'access': str(token.access_token)
        }
        return Response(data, status=status.HTTP_201_CREATED)


class StudentLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing students using their email and password.
    """
    permission_classes = (AllowAny,)
    serializer_class = StudentLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = StudentSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {
            'refresh': str(token),
            'access': str(token.access_token)
        }
        return Response(data, status=status.HTTP_200_OK)


class StudentLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(RetrieveAPIView):
    """
    An endpoint to get information of an authenticated student
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentSerializer

    def get_object(self):
        return self.request.user
