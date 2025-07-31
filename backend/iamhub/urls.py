from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nft/', views.nft_upload, name='nft_upload'),
    path('users/', views.user_profile, name='user_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
]