from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from .models import Post
from django.contrib.auth.models import User
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
		'posts': Post.objects.all()
	}
	#return HttpResponse('<h1> Blog Home</h1>')
	return render(request, 'html/home.html', Context)
@login_required
def about(request):
	#return HttpResponse('<h1> Blog About</h1>')
	
	return render(request, 'html/about.html')

@login_required
def post(request):
	if(request.method=='GET'):
		return render(request, 'html/post.html')
	elif(request.method=='POST'):
		ttl= request.POST.get('title','')
		txt= request.POST.get('text','')
		auth= request.POST.get('author','')

		u=User(username=auth)
		u.save()

		p=Post(title=ttl, text=txt, author=u)
		p.save()

		return redirect('blog-home')

@login_required
def edit(request, id):

	p=Post.objects.get(id=id)
	if(request.method=='GET'):
		Context={
			'post': p
		}
		return render(request, 'html/edit.html', Context)

	elif(request.method=='POST'):

		p.title= request.POST.get('title','')
		p.text= request.POST.get('text','')
		p.author.username= request.POST.get('author','')

		p.author.save()
		p.save()

		return redirect('blog-home')
	

def delete(request, id):
	Post.objects.get(id=id).delete()
	return redirect('blog-home')

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

def allPost(request):

	posts= list(Post.objects.all().values())

	return JsonResponse(posts, safe=False)