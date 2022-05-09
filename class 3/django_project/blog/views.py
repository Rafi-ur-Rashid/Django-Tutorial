from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

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
		'posts': Post.objects.filter(title__contains='2')
	}
	#return HttpResponse('<h1> Blog Home</h1>')
	return render(request, 'html/home.html', Context)

def about(request):
	#return HttpResponse('<h1> Blog About</h1>')
	
	return render(request, 'html/about.html')