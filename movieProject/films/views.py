from django.shortcuts import render, redirect
from .models import News_post, New_film
from .forms import New_filmForm, News_postForm

def index(request):
    news = News_post.objects.all()
    films = New_film.objects.all()
    return render(request, 'films/index.html', {'news': news, 'films': films})

def add_films(request):
    error = ''
    if request.method == 'POST':
        form = New_filmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Введены некорректные данные'
    form = New_filmForm()
    return render(request, 'films/add_films.html', {'form': form, 'error': error})

def add_news(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Введены некорректные данные'
    form = News_postForm()
    return render(request, 'films/add_news.html', {'form': form, 'error': error})
