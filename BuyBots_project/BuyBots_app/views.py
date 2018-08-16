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
    category = get_object_or_404(Category, name=name_category)
    bots = Bot.objects.filter(id_category=category.pk)
    return render(
        request, "BuyBots_app/bot_category.html", {"category": category, "bots": bots}
    )


def lk(request):
    bots = Bot.objects.filter()
    return render(request, "BuyBots_app/lk.html", {"bots": bots})


def add_bot(request):

    if request.method == "POST":
        form = AddBotForm(request.POST)
        if form.is_valid():
            bot = form.save(commit=False)
            bot.developer = request.user
            bot.save()
    else:
        form = AddBotForm()
    return render(request, "BuyBots_app/add_bot.html", {"form": form})
