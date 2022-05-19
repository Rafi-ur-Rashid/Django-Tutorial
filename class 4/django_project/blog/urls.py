
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
 	path('about/', views.about, name='blog-about'),
    path('login/', views.signin, name='blog-login'),
    path('logout/', views.signout, name='blog-logout')
    
       
]
