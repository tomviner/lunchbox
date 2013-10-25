from django.conf.urls import patterns, url

from core.views import PersonView


urlpatterns = patterns('',
    url(r'^$', PersonView.as_view(), name='home'),
)
