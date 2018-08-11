from django import forms

from .models import Bot


class AddBotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ('name', 'price', 'description')
