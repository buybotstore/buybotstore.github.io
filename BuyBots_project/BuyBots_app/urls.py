from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.bot_list, name='bot_list'),
    url(r'^developer/(?P<developer>[A-Za-z]+[ ]*[A-Za-z]*)/$', views.bot_developer, name='bot_developer'),
    url(r'^category/(?P<name_category>[A-Za-z]*[ ]*[A-Za-z]*[А-Яа-я]*[ ]*[А-Яа-я]*)/$', views.bot_category, name='bot_category'),
    url(r'^(?P<en_name>[A-Za-z]+[ ]*[A-Za-z]*)/$', views.bot_detail, name='bot_detail'),   
    url(r'lk/', views.lk, name='lk'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^bot/add/$', views.add_bot, name='add_bot')
]