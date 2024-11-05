from django.db import models


class Films(models.Model):
    GENRE_CHOICE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Боевик', 'Боевик')
    )
    image = models.ImageField(upload_to='film/', verbose_name='Загрузите картинку')
    title = models.CharField(max_length=100, verbose_name='Укажите название фильма')
    price = models.FloatField(verbose_name='Укажите цену фильма')
    start_film = models.DateField(verbose_name='Укажите дату выхода фильма')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE,default='Комедия', verbose_name='Укажите жанр фильма')

    time_ = models.TimeField(verbose_name='Укажите время продолжительнысти фильма')
    director = models.CharField(max_length=30, verbose_name='Укажите режиссер фильма')
    trailer = models.URLField(verbose_name='Укажите ссылку на трейлер фильма')