from django import forms
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class UserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'core/person_list.html'
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context


class LoginView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        authed_user = authenticate(username=self.object.username, password=None)
        login(request, authed_user)
        return redirect('/')


class LogoutView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        logout(request)
        self.request = request
        return redirect('/')
