from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.nft_upload.views import upload_nft_view, upload_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_nft_view, name='upload_nft'),
    path('success/', upload_success, name='upload_success'),
    path('accounts/', include('allauth.urls')),
    path('grappelli/', include('grappelli.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)