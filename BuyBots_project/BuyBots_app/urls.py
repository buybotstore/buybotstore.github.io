from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.bot_list, name='bot_list'),
    url(r'^bot/sort-developer/(?P<pk>\d+)/$', views.bot_developer, name='bot_developer'),
    url(r'^bot/sort-category/(?P<pk>\d+)/$', views.bot_category, name='bot_category'),
    url(r'^bot/(?P<pk>\d+)/$', views.bot_detail, name='bot_detail'),
    url(r'lk/', views.lk, name='lk'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^bot/(?P<pk>\d+)/$', views.bot_detail, name='bot_detail'),
    url(r'^bot/add/$', views.add_bot, name='add_bot')
]
