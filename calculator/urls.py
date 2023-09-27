
from django.urls import path , include
from .views import index
app_name="calculator"
urlpatterns = [

    path('', index,name="index")
]
