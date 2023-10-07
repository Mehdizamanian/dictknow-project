from django.shortcuts import render
import requests
from PyDictionary import PyDictionary

def index(request):
    return render(request,'dictionary/index.html')

def search(request):
    word = request.GET['word']
    # res=request.get('https://www.dictionary.com/browse/order')
    return render(request,'dictionary/topics-listing.html',{'word':word})


# Create your views here.
