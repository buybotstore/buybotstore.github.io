from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Bot
from .models import Developer
from .models import Category
def bot_list(request):
   
    bots=Bot.objects.filter()
     
    return render(request, 'BuyBots_app/bot_list.html', {'bots': bots})
def bot_detail(request, pk):
    bots = get_object_or_404(Bot, pk=pk)
    return render(request, 'BuyBots_app/bot_detail.html', {'bots': bots})
def bot_developer(request, pk):
    developer =get_object_or_404(Developer, pk=pk)
    bots=Bot.objects.filter(id_developer=pk)
    return render(request, 'BuyBots_app/bot_developer.html', {'developer': developer,'bots':bots})
def bot_category(request, pk):
    category =get_object_or_404(Category, pk=pk)
    bots=Bot.objects.filter(id_category=pk)
    return render(request, 'BuyBots_app/bot_category.html', {'category': category,'bots':bots})