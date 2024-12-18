from django.shortcuts import render
from news.models import News,SliderHomepage, PaymentMethod


def homepage(request):
    services = News.objects.all()
    sliders = SliderHomepage.objects.all()
    context = {
        'services':services,
        'sliders':sliders,
    }
    return render(request, 'index.html',context)

def mkassaPage(request): 
    paymet = PaymentMethod.objects.all()
    context = {
        'paymet':paymet
    }
    return render(request, 'mkassa.html',context)

def installmentPage(request):
    return render(request, 'installment_plan.html')