from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^parsel/upload', views.upload, name='upload'),
        url(r'^parsel/list', views.list, name='list'),

]
