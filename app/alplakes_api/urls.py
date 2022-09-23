from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_api import urls as rest_urls

from upload.views import image_upload

urlpatterns = [
    path("admin/", admin.site.urls),
    path("upload/", image_upload, name="upload"),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(rest_urls)),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
