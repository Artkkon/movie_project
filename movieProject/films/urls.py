from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_films/', views.add_films, name='add_films'),
    path('add_news/', views.add_news, name='add_news'),
    ]