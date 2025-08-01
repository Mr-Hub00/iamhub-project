from django.shortcuts import render, redirect
from .forms import UploadNFTForm
from .models import NFTAsset
from ipfs_upload.pin_to_ipfs import pin_file_to_ipfs
import tempfile
import os

def upload_nft_view(request):
    if request.method == 'POST':
        form = UploadNFTForm(request.POST, request.FILES)
        if form.is_valid():
            nft = form.save(commit=False)
            image_file = request.FILES['image']
            # Save image temporarily to get file path
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in image_file.chunks():
                    temp_file.write(chunk)
                temp_path = temp_file.name
            # Pin to IPFS
            ipfs_cid = pin_file_to_ipfs(temp_path)
            nft.ipfs_cid = ipfs_cid
            nft.save()
            os.remove(temp_path)  # Clean up temp file
            return redirect('nft_upload_success')
    else:
        form = UploadNFTForm()
    return render(request, 'nft_upload/upload.html', {'form': form})

def upload_success(request):
    return render(request, 'nft_upload/success.html')