from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.bot_list, name='bot_list'),
<<<<<<< HEAD
    url(r'^developer/(?P<developer>[A-Za-z]+[ ]*[A-Za-z]*)/$', views.bot_developer, name='bot_developer'),
    url(r'^category/(?P<name_category>[A-Za-z]*[ ]*[A-Za-z]*[А-Яа-я]*[ ]*[А-Яа-я]*)/$', views.bot_category, name='bot_category'),
    url(r'^(?P<en_name>[A-Za-z]+[ ]*[A-Za-z]*)/$', views.bot_detail, name='bot_detail'),   
    url(r'lk/', views.lk, name='lk'),
=======
    url(r'^bot/sort-developer/(?P<pk>\d+)/$', views.bot_developer, name='bot_developer'),
    url(r'^bot/sort-category/(?P<pk>\d+)/$', views.bot_category, name='bot_category'),
    url(r'^bot/(?P<pk>\d+)/$', views.bot_detail, name='bot_detail'),
    url(r'private/', views.private_cabinet, name='private_cabinet'),
>>>>>>> a43202a89ab6e17bc0b15dfb5a01e11f36bdf040
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^bot/add/$', views.add_bot, name='add_bot')
]