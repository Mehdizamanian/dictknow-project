
from .views import bmiView
from django.urls import path 

app_name="bmi"

urlpatterns = [

    path('', bmiView , name="bmiview"),
]
