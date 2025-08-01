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
    return HttpResponse("Welcome to IAMHub!")

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
    return HttpResponse("Dashboard Page (placeholder)")

def upload_success(request):
    return render(request, 'nft_upload/success.html')