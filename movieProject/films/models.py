from django.db import models

class News_post(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    discription = models.CharField('Описание', max_length=250)
    text = models.TextField('Новость')
    date = models.DateTimeField('Дата публикации')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


