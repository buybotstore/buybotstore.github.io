from django.shortcuts import render
from django.utils import timezone
from .models import Bot
 
def bot_list(request):
   
    bots=Bot.objects.filter()
    return render(request, 'BuyBots_app/bot_list.html', {'bots': bots})