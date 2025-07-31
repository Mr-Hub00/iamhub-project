from django.urls import path, include
from . import views

urlpatterns = [
    path('upload/', views.upload_nft, name='nft_upload'),
    path('success/', views.upload_success, name='nft_upload_success'),
    path('nft/', include('apps.nft_upload.urls')),
]