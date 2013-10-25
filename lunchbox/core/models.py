from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=256, blank=False, default='')\


    def __str__(self):
        return self.name

class Vote (models.Model):
    date = models.DateField(auto_now_add=True)
    person = models.ForeignKey(Person)
    restaurant = models.ForeignKey(Restaurant)
