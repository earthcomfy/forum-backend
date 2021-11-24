from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserRegisterationAPIView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterationAPIView.as_view(), name="create_user"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
