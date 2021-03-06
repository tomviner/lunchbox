from django.conf.urls import patterns, url

from core.views import cast_vote, LoginView, LogoutView, test_vote, UserView, ResultView
from core.views import get_votes

urlpatterns = patterns('',
   url(r'^$', UserView.as_view(), name='home'),
   url(r'login/(?P<pk>\d+)/$',
       LoginView.as_view(), name='login'),
   url(r'logout/(?P<pk>\d+)/$',
       LogoutView.as_view(), name='logout'),
   url(r'^testvote/$', test_vote),
   url(r'^vote/$', cast_vote),
   url(r'^getvotes/$', get_votes),
   url(r'^results/$', ResultView.as_view()),
)
