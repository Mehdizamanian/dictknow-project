from django.shortcuts import render
import requests
from PyDictionary import PyDictionary

def index(request):
    return render(request,'dictionary/index.html')

def search(request):
    word = request.GET.get('word')
    dictionary=PyDictionary()
    meaning =dictionary.meaning(word)
    synonyms =dictionary.synonym(word)
    antonyms = dictionary.antonym(word)

    
    context ={
        'word':word , 
        'meaning':meaning['Noun'][0],
        'synonyms':synonyms,
        'antonyms':antonyms,
    }

    return render(request,'dictionary/topics-listing.html',context)

    print (dictionary.antonym("Life"))
# Create your views here.
