from django import forms
from .models import *

class AppointmentForm(forms.Form):
   name = forms.CharField(min_length=2, label="Ваше имя", widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
   number = forms.CharField(min_length=10, label="Номер телефона", widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'}))
   branch = forms.ModelChoiceField(queryset=Branchoffice.objects.all(), label="Филиал", empty_label="Выберите филиал")




