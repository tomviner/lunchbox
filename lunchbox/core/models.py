from django.contrib.auth.models import User
from django.db import models


class Restaurant(models.Model):
    url = models.CharField(max_length=2048, blank=False, default='')
    name = models.CharField(max_length=256, blank=False, default='')


    def __str__(self):
        return self.name


class Vote (models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
