from django.conf.urls import patterns, url
from AppRating import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^recommend/', views.editorRecommend, name='recommend'),
                       url(r'^ranklist/',views.rankList,name='ranklist'),
                       url(r'^newarrival/',views.newArrival,name='newarrival'),
                       url(r'^categories/',views.categories,name='categories'),
                       url(r'^register/$', views.register, name='register'),
                       )
