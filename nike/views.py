from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'homedesign/index.html')

def find_store(request):
    return render(request,'homedesign/find-store.html')

def help(request):
    return render(request,'homedesign/help.html')

def join_us(request):
    return render(request,'homedesign/join-us.html')

def sign_in(request):
    return render(request,'homedesign/sign-in.html')
