from django.shortcuts import render
from django.views.generic import CreateView, ListView


from .models import Person



class ListPerson(ListView):
    model = Person
    template_name = 'resturant_picker/login.html'

class CreatePerson(CreateView):
    model = Person