from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appearance.urls')),
    path('api/', include('appearance.api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
