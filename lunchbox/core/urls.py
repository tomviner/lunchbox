from django.conf.urls import patterns, url

from core.views import UserView, LoginView

urlpatterns = patterns('',
    url(r'^$', UserView.as_view(), name='home'),
    url(r'login/(?P<pk>\d+)/$', LoginView.as_view(), name='login'),
)
