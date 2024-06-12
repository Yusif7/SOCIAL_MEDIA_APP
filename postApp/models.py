from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    # Поле caption используется для хранения текстового описания или подписи к посту.
    caption = models.TextField(blank=True)
    # "Slug" – это человекочитаемая часть URL, которая обычно формируется из заголовка поста
    # дополнительные валидации для обеспечения корректного формата slug (только буквы, цифры, дефисы и подчёркивания)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    """
    *args - Это позволяет передавать произвольное количество позиционных аргументов функции.
    *args собирает все позиционные аргументы в кортеж.
    **kwargs — Это позволяет передавать произвольное количество именованных (ключевых) аргументов функции.
    **kwargs собирает все именованные аргументы в словарь.
    """

    def save(self, *args, **kwargs):
        if not self.slug:
            # slugify, которая преобразует строку в формат "slug" — заменяет пробелы дефисами, приводит строку к нижнему регистру и удаляет недопустимые символы.
            self.slug = slugify(self.title)
        # вызывается оригинальный метод save из суперкласса (models.Model) и фактически сохраняет объект в базу данных.
        super().save(*args, **kwargs)
