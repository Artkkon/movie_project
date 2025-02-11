from django.db import models

class News_post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    discription = models.CharField('Описание', max_length=250)
    text = models.TextField('Новость')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class New_film(models.Model):
    title = models.CharField('Название', max_length=50)
    discription = models.TextField('Описание')
    text = models.TextField('Отзыв')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


