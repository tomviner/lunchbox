from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView

from core.models import Restaurant, Vote


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
        authed_user = authenticate(
            username=self.object.username, password=None)
        login(request, authed_user)
        return redirect('/')


class LogoutView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        logout(request)
        return redirect('/')


def test_vote(request):
    context = {}
    context["object_list"] = Restaurant.objects.all()
    return render(request, "core/test_vote.html", context)


def cast_vote(request):
    person_id = 1
    rest_id = request.POST["restaurant"]
    vote, created = Vote.objects.get_or_create(
        restaurant_id=rest_id, person_id=person_id)
    if created:
        vote.save()
        return HttpResponse("ok")
    else:
        vote.delete()
        return HttpResponse("remove")
