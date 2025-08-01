from django.shortcuts import render, redirect
from .forms import UploadNFTForm
from .models import NFTAsset
from ipfs_upload.pin_to_ipfs import pin_file_to_ipfs

def upload_nft_view(request):
    if request.method == 'POST':
        form = UploadNFTForm(request.POST, request.FILES)
        if form.is_valid():
            nft = form.save(commit=False)
            uploaded_file = request.FILES['image']
            temp_path = f"/tmp/{uploaded_file.name}"

            # Save file temporarily
            with open(temp_path, 'wb+') as temp_file:
                for chunk in uploaded_file.chunks():
                    temp_file.write(chunk)

            # Pin to IPFS
            cid = pin_file_to_ipfs(temp_path)
            nft.ipfs_cid = cid  # Make sure your model field is named ipfs_cid
            nft.save()

            return render(request, 'nft_upload/upload_success.html', {'cid': cid})
    else:
        form = UploadNFTForm()
    
    return render(request, 'nft_upload/upload.html', {'form': form})

def upload_success(request):
    return render(request, 'nft_upload/success.html')