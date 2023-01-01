from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('user.urls')),
    path('home/user-auth/', include('rest_framework.urls'))
]
