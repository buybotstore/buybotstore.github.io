from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Bot
from .models import Developer
from .models import Category
from .models import Comment
from .models import Response
from .add_bot_form import AddBotForm


def bot_list(request):
    bots = Bot.objects.filter()
    return render(request, 'BuyBots_app/bot_list.html', {'bots': bots})

def bot_detail(request, pk):
    bots = get_object_or_404(Bot, pk=pk)
    comments = Comment.objects.filter(id_bot=pk)
    return render(request, 'BuyBots_app/bot_detail.html', {'bots': bots, 'comments': comments})

def bot_developer(request, pk):
    developer = get_object_or_404(Developer, pk=pk)
    bots = Bot.objects.filter(id_developer=pk)
    return render(request, 'BuyBots_app/bot_developer.html', {'developer': developer, 'bots': bots})

def bot_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    bots = Bot.objects.filter(id_category=pk)
    return render(request, 'BuyBots_app/bot_category.html', {'category': category, 'bots': bots})

def private_cabinet(request):
    '''Личный кабинет для разработчика'''
    bots = Bot.objects.filter()
    return render(request, 'BuyBots_app/private_cabinet.html', {'bots': bots})    

def add_bot(request):
    '''Представления для добавления бота'''
    if request.method == "POST": # если данные были переданы
        form = AddBotForm(request.POST) # инициализируем форму с этими данными
        if form.is_valid(): # если форма корректна
            bot = form.save(commit=False) # сохраняем форму, но указав commit=False, не сохраняем модель
            bot.developer = request.user # потому что сначала добавим недостоющее поле - разработчик
            bot.save() # сохраняем модель
    else: # если же данные не были переданы
        form = AddBotForm() # создаем пустую форму
    return render(request, 'BuyBots_app/add_bot.html', {'form': form}) # возвращаем html-страницу

