from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/question/', include('qa.urls', namespace='question')),
]

# Media Assets
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
