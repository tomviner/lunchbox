from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=256, blank=False, default='')\


    def __str__(self):
        return self.name

class Vote (models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
