from django.views.generic import CreateView, ListView


from .models import Person


class ListPerson(ListView):
    model = Person


class CreatePerson(CreateView):
    model = Person
