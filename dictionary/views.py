from django.shortcuts import render

def indexView(request):
    return render(request,'dictionary/index.html')

def searchView(request):
    return render(request,'dictionary/topics-listing.html')


# Create your views here.
