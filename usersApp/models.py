from django.db import models
from django.conf import settings


class Profile(models.Model):
    # OneToOneField создаёт связь один-к-одному с моделью пользователя, указанной в settings.AUTH_USER_MODEL
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #
    photo = models.ImageField(upload_to='usersApp/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username
