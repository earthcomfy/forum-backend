from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.StudentRegisterationAPIView.as_view(),
         name="create_student"),
    path('login/', views.StudentLoginAPIView.as_view(), name="login_student"),
    path('student/', views.StudentAPIView.as_view(), name="get_student"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.StudentLogoutAPIView.as_view(), name='logout_student')
]
