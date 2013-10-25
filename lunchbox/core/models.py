from django.db import models


class Restaurant(models.Model):
    pass


class Vote (models.Model):
    date = models.DateField(auto_now_add=True)
    people = models.ManyToManyField(Person)
