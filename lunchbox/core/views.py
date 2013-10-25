from django.views.generic import CreateView


from .models import Person


class PersonView(CreateView):
    model = Person
    template_name = 'core/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Person.objects.all()
        return context