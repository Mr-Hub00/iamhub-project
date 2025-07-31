from django.shortcuts import render, redirect
from django import forms
from .models import NFTAsset
from pin_to_ipfs import pin_file_to_ipfs

class NFTAssetForm(forms.ModelForm):
    class Meta:
        model = NFTAsset
        fields = ['title', 'description', 'image']

def upload_nft(request):
    if request.method == 'POST':
        form = NFTAssetForm(request.POST, request.FILES)
        if form.is_valid():
            nft = form.save(commit=False)
            nft.image.file.seek(0)
            temp_path = nft.image.file.temporary_file_path()
            ipfs_cid = pin_file_to_ipfs(temp_path)
            nft.ipfs_cid = ipfs_cid
            nft.save()
            return redirect('nft_upload_success')
    else:
        form = NFTAssetForm()
    return render(request, 'nft_upload/upload.html', {'form': form})

def upload_success(request):
    return render(request, 'nft_upload/success.html')