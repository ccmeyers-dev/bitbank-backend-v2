from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ccmeyers100/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/users/', include('broker.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
