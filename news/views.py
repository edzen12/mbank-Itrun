from django.shortcuts import render
from news.models import News,SliderHomepage


def homepage(request):
    services = News.objects.all()
    sliders = SliderHomepage.objects.all()
    context = {
        'services':services,
        'sliders':sliders,
    }
    return render(request, 'index.html',context)

def mkassaPage(request): 
    return render(request, 'mkassa.html')