from django.shortcuts import render
import telepot
from .models import *
from .forms import*

def mainpage(request):
    services = Services.objects.all()
    address = Branchoffice.objects.all()
    city = City.objects.all()
    form = AppointmentForm()

    context = {
        'services': services,
        'address': address,
        'city': city,
        'form': form,
    }

    if request.method == 'POST':
        token = '6439290351:AAFhjBfP7aoWqSOTUF1r0RSsiFQ_HJwgd1c'
        Bot = telepot.Bot(token)
        form1 = AppointmentForm(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['name']
            number = form1.cleaned_data['number']
            message = f'Имя: {name} \nНомер телефона: {number}'
        Bot.sendMessage(685875132, message)
        context ['success'] =  'Ваша заявка отправлена'

    return render(request, 'mainapp/index.html', context=context)