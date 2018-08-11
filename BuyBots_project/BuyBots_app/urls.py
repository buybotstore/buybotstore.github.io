from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bot_list, name='bot_list'),
     url(r'^bot/(?P<pk>\d+)/$', views.bot_detail, name='bot_detail'),
     url(r'^bot/add/$', views.add_bot, name='add_bot')
]
