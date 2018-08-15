from django import forms
from .models import Bot
from .models import Category


class AddBotForm(forms.ModelForm):
    '''Форма добавления бота'''
    class Meta:
        model = Bot # указываем модель, поля которой будем отображать
        fields = ('name_bot', 'name_category', 'price', 'description') # поля, которые будут отображены

    def __init__(self, *args, **kwargs):
        '''Перегруженный конструктор для заполнения выпадающего списка'''
        super().__init__(*args, **kwargs)
        self.fields['name_category'].queryset = Category.objects.all() # заполняем выпадающий список
                                                                       # имеющимися объектами