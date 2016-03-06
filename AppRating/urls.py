from django.conf.urls import patterns, url
from AppRating import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index')
                       )
