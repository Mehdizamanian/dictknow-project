
from django.urls import path 
from .views import indexView, searchView

app_name="dictionary"

urlpatterns = [
    path('', indexView,name='index'),
    path('search/', searchView,name='search'),
]
