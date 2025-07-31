from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import NFTAsset
from django import forms

class NFTAssetForm(forms.ModelForm):
    class Meta:
        model = NFTAsset
        fields = ['title', 'description', 'image']

def home(request):
    return HttpResponse("Welcome to IAMHub!")

def upload_nft(request):
    if request.method == 'POST':
        form = NFTAssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nft_upload_success')
    else:
        form = NFTAssetForm()
    return render(request, 'nft_upload/upload.html', {'form': form})

def user_profile(request):
    return HttpResponse("User Profile Page (placeholder)")

def dashboard(request):
    return HttpResponse("Dashboard Page (placeholder)")

def upload_success(request):
    return render(request, 'nft_upload/success.html')