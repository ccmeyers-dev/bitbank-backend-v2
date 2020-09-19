from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ccmeyers100/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/users/', include('broker.urls'))
]
