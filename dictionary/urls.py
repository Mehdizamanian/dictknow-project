
from django.urls import path 
from .views import dictView

app_name="dictionary"

urlpatterns = [

    path('', dictView,name='dictview'),
]
