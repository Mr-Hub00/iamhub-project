from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to IAMHub!")

def nft_upload(request):
    return HttpResponse("NFT Upload Page (placeholder)")