from django.shortcuts import render

def index(request):
    return render(request,'dictionary/index.html')

def search(request):
    word = request.GET['word']
    return render(request,'dictionary/topics-listing.html',{'word':word})


# Create your views here.
