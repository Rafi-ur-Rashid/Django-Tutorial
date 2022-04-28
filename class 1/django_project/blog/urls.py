
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
 	path('about/<name>', views.about),
       
]
