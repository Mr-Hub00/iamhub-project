from django import forms
from .models import NFTAsset

class UploadNFTForm(forms.ModelForm):
    class Meta:
        model = NFTAsset
        fields = ['title', 'description', 'image']