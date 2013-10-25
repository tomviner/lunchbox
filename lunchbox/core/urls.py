from django.conf.urls import patterns, url
from core.views import UserView, LoginView, LogoutView
from core.views import cast_vote
from core.views import test_vote

urlpatterns = patterns('',
    url(r'^$', UserView.as_view(), name='home'),
    url(r'login/(?P<pk>\d+)/$', LoginView.as_view(), name='login'),
    url(r'logout/(?P<pk>\d+)/$', LogoutView.as_view(), name='logout'),
    url(r'^testvote/$', test_vote),
    url(r'^vote/$', cast_vote),
)
