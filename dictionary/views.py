from django.shortcuts import render

def index(request):
    return render(request,'dictionary/index.html')

def search(request):
    return render(request,'dictionary/topics-listing.html')


# Create your views here.
