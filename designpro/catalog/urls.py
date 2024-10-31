from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^profile/$', views.ProfilePage, name='profile'),
]