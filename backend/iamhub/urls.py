from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.nft_upload.views import upload_nft_view, upload_success
from iamhub.views import home, champion_profile_view, dashboard, login_view, register_view

urlpatterns = [
    path('', home, name='home'),
    path('champion-profile/', champion_profile_view, name='champion_profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),
    path('upload/', upload_nft_view, name='upload_nft'),
    path('success/', upload_success, name='upload_success'),
    
    # Clean JWT Authentication endpoints
    path('api/auth/', include('apps.users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)