from django.shortcuts import render
from news.models import News,SliderHomepage, PaymentMethod, Category, Partners


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
    category = Category.objects.all()
    patners = Partners.objects.all()
    context = {
        'categories':category, 
        'patners':patners, 
    }
    return render(request, 'installment_plan.html', context)