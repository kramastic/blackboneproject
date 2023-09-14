from django.shortcuts import render
import telepot
from .models import *
from .forms import*


# Create your views here.

def mainpage(request):
    services = Services.objects.all()
    address = Branchoffice.objects.all()
    form = AppointmentForm()

    context = {
        'services': services,
        'address': address,
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



# def send_mess(name):
#     token = '6439290351:AAFhjBfP7aoWqSOTUF1r0RSsiFQ_HJwgd1c'
#     Bot = telepot.Bot(token)
#     form1 = AppointmentForm(request.POST)
#     if form.is_valid():
#         name = form1.cleaned_data('name')
#     Bot.sendMessage(685875132, f'{name}')
#




# def appointment(request):
#     context = {}
#     if request.method == 'POST':
#         pass
#     else:
#         form = AppointmentForm()
#         context['form'] = form
#     return render(request,'mainapp/index.html', context=context)

# def sendinfo(request):
#     if request.method == 'POST':
#         token = '6439290351:AAFhjBfP7aoWqSOTUF1r0RSsiFQ_HJwgd1c'
#         my_id = 685875132
#         Bot = telepot.Bot(token)
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#         Bot.sendMessage(685875132, name)
#         return render(request, 'mainapp/index.html', context=name)

        # send_message(form.cleaned_data['name'], form.cleaned_data['number'], form.cleaned_data['branch'])
        #     name = form.cleaned_data.get('name')
        # number = form.cleaned_data['number']
        # branch = form.cleaned_data['branch']
        # text = f'{name}, {number}, {branch}'
    #     Bot.sendMessage(685875132, name)
    # # context = {}
    # if request.method == 'POST':
    #     form = AppointmentForm(request.POST)
    #     if form.is_valid():
    #         send_message(form.cleaned_data['name'], form.cleaned_data['number'], form.cleaned_data['branch'])
    #         context = {'success' : 1}
    # else:
    #     form = AppointmentForm()
    # context['form'] = form
    # return render(request, 'mainapp/index.html', context=name)

# def send_message(name, number, branch):
#     token = '6439290351:AAFhjBfP7aoWqSOTUF1r0RSsiFQ_HJwgd1c'
#     my_id = 685875132
#     Bot = telepot.Bot(token)
#     text = f'{name}, {number}, {branch}'
#     Bot.sendMessage(685875132, text, parse_mode="Markdown")
