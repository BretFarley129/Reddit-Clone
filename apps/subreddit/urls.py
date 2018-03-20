from django.conf.urls import url
from . import views

print "IN SUBREDDIT URLS"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/test$', views.test),
    url(r'^/$', views.index),
    url(r'^', views.nothing),
]