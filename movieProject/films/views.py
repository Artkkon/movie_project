from django.shortcuts import render
from .models import News_post

def index(request):
    news = News_post.objects.all()
    return render(request, 'films/index.html', {'news': news})

def add_films(request):
    return render(request, 'films/add_films.html')

def add_news(request):
    return render(request, 'films/add_news.html')
