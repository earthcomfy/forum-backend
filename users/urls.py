from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import StudentLogoutAPIView, StudentRegisterationAPIView, StudentLoginAPIView, StudentAPIView

app_name = 'users'

urlpatterns = [
    path('register/', StudentRegisterationAPIView.as_view(), name="create_student"),
    path('login/', StudentLoginAPIView.as_view(), name="login_student"),
    path('student/', StudentAPIView.as_view(), name="get_student"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', StudentLogoutAPIView.as_view(), name='blacklist')
]
