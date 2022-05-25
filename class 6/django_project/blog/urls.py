
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
 	path('about/', views.about, name='blog-about'),
    path('login/', views.signin, name='blog-login'),
    path('logout/', views.signout, name='blog-logout'),
    path('post/', views.post, name='blog-post'),
    path('delete/<int:id>', views.delete, name='blog-delete'),
    path('edit/<int:id>', views.edit, name='blog-edit'),
    path('allPost/', views.allPost),
    
       
]
