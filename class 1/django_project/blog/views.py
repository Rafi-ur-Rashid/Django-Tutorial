from django.shortcuts import render
from django.http import HttpResponse


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
def home(request):
	Context={
		'posts': posts
	}
	#return HttpResponse('<h1> Blog Home</h1>')
	return render(request, 'html/home.html', Context)

def about(request, name):
	#return HttpResponse('<h1> Blog About</h1>')
	Context={
		'name': name
	}
	return render(request, 'html/about.html', Context)