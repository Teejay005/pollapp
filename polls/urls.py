# from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, url
from django.contrib import admin
from polls import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.ResultView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
