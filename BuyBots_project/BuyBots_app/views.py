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
    return render(request, "BuyBots_app/bot_list.html", {"bots": bots})


def bot_detail(request, en_name):
    bots = get_object_or_404(Bot, en_name=en_name)
    # comments = Comment.objects.filter(id_bot=pk)
    return render(request, "BuyBots_app/bot_detail.html", {"bots": bots})


def bot_developer(request, developer):
    developers = get_object_or_404(Developer, en_full_name=developer)
    bots = Bot.objects.filter(id_developer=developers.pk)
    return render(
        request,
        "BuyBots_app/bot_developer.html",
        {"developer": developers, "bots": bots},
    )


def bot_category(request, name_category):
    category = get_object_or_404(Category, name_category=name_category)
    bots = Bot.objects.filter(name_category=category.pk)
    return render(
        request, "BuyBots_app/bot_category.html", {"category": category, "bots": bots}
    )


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

