from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


from .models import Person


class PersonView(CreateView):
    model = Person
    template_name = 'core/person_list.html'
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Person.objects.all()
        return context