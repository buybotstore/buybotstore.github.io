from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Bot
from .add_bot_form import AddBotForm


def bot_list(request):
    bots = Bot.objects.filter()
    return render(request, 'BuyBots_app/bot_list.html', {'bots': bots})

def bot_detail(request, pk):
    bots = get_object_or_404(Bot, pk=pk)
    return render(request, 'BuyBots_app/bot_detail.html', {'bots': bots})

def add_bot(request):
    if request.method == "POST":
        form = AddBotForm(request.POST)
        if form.is_valid():
            bot = form.save(commit=False)
            bot.developer = request.user
            bot.save()
    else:
        form = AddBotForm()
    return render(request, 'BuyBots_app/add_bot.html', {'form': form})
