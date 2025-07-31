from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to IAMHub!")

def nft_upload(request):
    return HttpResponse("NFT Upload Page (placeholder)")

def user_profile(request):
    return HttpResponse("User Profile Page (placeholder)")

def dashboard(request):
    return HttpResponse("Dashboard Page (placeholder)")