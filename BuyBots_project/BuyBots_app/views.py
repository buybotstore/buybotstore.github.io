from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Bot
 
def bot_list(request):
   
    bots=Bot.objects.filter()
    return render(request, 'BuyBots_app/bot_list.html', {'bots': bots})
def bot_detail(request, pk):
    bots = get_object_or_404(Bot, pk=pk)
    return render(request, 'BuyBots_app/bot_detail.html', {'bots': bots})