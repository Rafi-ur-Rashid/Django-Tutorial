from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import Post

from django.contrib.auth.decorators import login_required

# Create your views here.
posts=[ 
	{
		'text': 'Hi this is my 1st text',
		'author': 'Rafi'
	},
	{
		'text': 'Hi this is my 2nd text',
		'author': 'Rafiq'
	} 
]

@login_required
def home(request):
	Context={
		'posts': Post.objects.filter(title__contains='2')
	}
	#return HttpResponse('<h1> Blog Home</h1>')
	return render(request, 'html/home.html', Context)
@login_required
def about(request):
	#return HttpResponse('<h1> Blog About</h1>')
	
	return render(request, 'html/about.html')

def signin(request):
	if(request.method=='GET'):
		return render(request, 'html/login.html')
	elif(request.method=='POST'):
		u= request.POST.get('username','')
		p= request.POST.get('password','')

		res=authenticate(username=u, password=p)

		if(res is None):
			return HttpResponse('<h1> Wrong Credentials! Sign in Failed </h1>')
		else:
			login(request, res)
			return redirect('blog-home')

def signout(request):
	logout(request)
	return redirect('blog-login')