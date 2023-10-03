from django import forms
from .models import *


class AppointmentForm(forms.Form):
    name = forms.CharField(min_length=2, label="Ваше имя",
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'formline'}))
    number = forms.CharField(min_length=10, label="Номер телефона",
                             widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона', 'class': 'formline'}))
    branch = forms.ModelChoiceField(queryset=OfficeBranch.objects.all(), empty_label="Адрес барбершопа",
                                    widget=forms.Select(attrs={'class': 'formline'}))
