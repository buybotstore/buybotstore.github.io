from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bot_list, name='bot_list'),
]