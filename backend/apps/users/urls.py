"""
URL patterns for JWT authentication and ChampionP profile management
"""
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import api_views

app_name = 'users'

urlpatterns = [
    # Authentication endpoints
    path('register/', api_views.register_view, name='register'),
    path('login/', api_views.login_view, name='login'),
    path('profile/', api_views.user_profile_view, name='profile'),
    
    # JWT token management
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Profile management endpoints
    path('update-wallet/', api_views.update_wallet_view, name='update_wallet'),
    path('update-profile/', api_views.update_profile_view, name='update_profile'),
    path('update-skills/', api_views.update_skills_view, name='update_skills'),
    
    # Community & networking endpoints
    path('champions/', api_views.community_champions_view, name='champions'),
    
    # Web3 integration endpoints
    path('web3-connect/', api_views.web3_connect_view, name='web3_connect'),
]
