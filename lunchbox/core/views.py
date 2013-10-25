from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView

from core.models import Restaurant, Vote
from core.models import Vote
from core.models import Restaurant
import json

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


@login_required
@csrf_exempt
def cast_vote(request):
    person_id = 1
    rest_url = request.POST["restaurant"]
    restaurant, created = Restaurant.objects.get_or_create(url=rest_url)


    vote, created = Vote.objects.get_or_create(restaurant=restaurant, user=request.user)

    if created:
        vote.save()
        status = "add"
    else:
        vote.delete()
        status = "remove"

    votes = Vote.objects.filter(restaurant=restaurant).count()
    return HttpResponse(json.dumps({"status": status, "votes": votes}), content_type="application/json")


def get_votes(request):
    rest_url = request.REQUEST["restaurant"]
    restaurant, created = Restaurant.objects.get_or_create(url=rest_url)

    votes = Vote.objects.filter(restaurant=restaurant).count()
    return HttpResponse(json.dumps({"votes": votes}), content_type="application/json")


