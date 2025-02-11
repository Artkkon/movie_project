from .models import News_post, New_film
from django.forms import ModelForm, TextInput, Textarea

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'discription', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок новости'}),
            'discription': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст новости'}),
        }


class New_filmForm(ModelForm):
    class Meta:
        model = New_film
        fields = ['title', 'discription', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название фильма'}),
            'discription': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание фильма'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш отзыв'}),
        }
