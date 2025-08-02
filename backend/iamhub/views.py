from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.nft_upload.models import NFTAsset
from django import forms
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from ipfs_upload.pin_to_ipfs import pin_file_to_ipfs

class NFTAssetForm(forms.ModelForm):
    class Meta:
        model = NFTAsset
        fields = ['title', 'description', 'image']

def home(request):
    return HttpResponse("""
    <html>
    <head><title>IAMHub - ChampionP Identity Platform</title></head>
    <body style="font-family: Arial; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh;">
        <div style="text-align: center; max-width: 600px; margin: 0 auto;">
            <h1>🏆 Welcome to IAMHub</h1>
            <h2>ChampionP Identity Platform</h2>
            <p style="font-size: 1.2em; margin: 30px 0;">Build your complete digital identity with our revolutionary 6-pillar framework</p>
            
            <div style="margin: 40px 0;">
                <a href="/dashboard/" style="background: white; color: #667eea; padding: 15px 30px; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 10px; display: inline-block;">🎛️ Dashboard</a>
                <a href="/champion-profile/" style="background: rgba(255,255,255,0.9); color: #667eea; padding: 15px 30px; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 10px; display: inline-block;">� ChampionP Profile</a>
            </div>
            
            <div style="margin: 30px 0;">
                <a href="/login/" style="background: rgba(255,255,255,0.2); color: white; padding: 12px 25px; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 10px; display: inline-block;">🔐 Login</a>
                <a href="/register/" style="background: rgba(255,255,255,0.2); color: white; padding: 12px 25px; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 10px; display: inline-block;">📝 Register</a>
            </div>
            
            <div style="margin: 30px 0;">
                <a href="/admin/" style="background: rgba(255,255,255,0.2); color: white; padding: 12px 25px; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 10px; display: inline-block;">⚙️ Admin Panel</a>
                <a href="/upload/" style="background: rgba(255,255,255,0.2); color: white; padding: 12px 25px; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 10px; display: inline-block;">🎨 Upload NFT</a>
            </div>
            
            <div style="margin-top: 50px; background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;">
                <h3>🎯 ChampionP Framework</h3>
                <p>Purpose • Profile • Placement • Personality • Proficiency • Potential Connections</p>
            </div>
        </div>
    </body>
    </html>
    """)

def champion_profile_view(request):
    """Serve the ChampionP profile interface"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend', 'champion-profile.html')
    try:
        with open(frontend_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return HttpResponse(html_content)
    except FileNotFoundError:
        return HttpResponse("ChampionP Profile page not found. Please ensure frontend/champion-profile.html exists.", status=404)

def upload_nft(request):
    if request.method == 'POST':
        form = NFTAssetForm(request.POST, request.FILES)
        if form.is_valid():
            nft = form.save(commit=False)
            uploaded_file = request.FILES['image']
            
            # Save temp file to access file path
            temp_dir = "temp"
            os.makedirs(temp_dir, exist_ok=True)
            temp_path = os.path.join(temp_dir, uploaded_file.name)
            with open(temp_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            try:
                cid = pin_file_to_ipfs(temp_path)
                nft.cid = cid  # Make sure your NFTAsset model has a 'cid' field
                nft.save()
                os.remove(temp_path)
                return render(request, 'nft_upload/success.html', {'cid': cid})
            except Exception as e:
                return HttpResponse(f"IPFS upload failed: {str(e)}", status=500)
    else:
        form = NFTAssetForm()
    return render(request, 'nft_upload/upload.html', {'form': form})

def user_profile(request):
    return HttpResponse("User Profile Page (placeholder)")

def dashboard(request):
    """Serve the dashboard interface"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend', 'dashboard.html')
    try:
        with open(frontend_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return HttpResponse(html_content)
    except FileNotFoundError:
        return HttpResponse("Dashboard page not found. Please ensure frontend/dashboard.html exists.", status=404)

def upload_success(request):
    return render(request, 'nft_upload/success.html')

def login_view(request):
    """Serve the login interface"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend', 'login.html')
    try:
        with open(frontend_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return HttpResponse(html_content)
    except FileNotFoundError:
        return HttpResponse("Login page not found. Please ensure frontend/login.html exists.", status=404)

def register_view(request):
    """Serve the registration interface"""
    frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend', 'register.html')
    try:
        with open(frontend_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return HttpResponse(html_content)
    except FileNotFoundError:
        return HttpResponse("Registration page not found. Please ensure frontend/register.html exists.", status=404)