from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('user.urls')),
    path('home/', include('helpzone.urls')),
    path("home/", include("shrt_trm_ch.urls")),
    path('home/user-auth/', include('rest_framework.urls'))
]
