from django.conf.urls import patterns, include, url

from core.views import ListPerson, CreatePerson


urlpatterns = patterns('',
    url(r'^$', ListPerson.as_view(), name='home'),
)
