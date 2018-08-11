from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Bot
from .models import Developer
from .models import Category
from .models import Comment
from .models import Response
def bot_list(request):
   
    bots=Bot.objects.filter()
     
from .add_bot_form import AddBotForm


def bot_list(request):
    bots = Bot.objects.filter()
    return render(request, 'BuyBots_app/bot_list.html', {'bots': bots})

def bot_detail(request, pk):
    bots = get_object_or_404(Bot, pk=pk)
    comments=Comment.objects.filter(id_bot=pk)
    return render(request, 'BuyBots_app/bot_detail.html', {'bots': bots,'comments':comments})
def bot_developer(request, pk):
    developer =get_object_or_404(Developer, pk=pk)
    bots=Bot.objects.filter(id_developer=pk)
    return render(request, 'BuyBots_app/bot_developer.html', {'developer': developer,'bots':bots})
def bot_category(request, pk):
    category =get_object_or_404(Category, pk=pk)
    bots=Bot.objects.filter(id_category=pk)
    return render(request, 'BuyBots_app/bot_category.html', {'category': category,'bots':bots})
def lk(request ):
    bots=Bot.objects.filter()
    return render(request, 'BuyBots_app/lk.html',{'bots':bots})
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
