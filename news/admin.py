from django.contrib import admin
from .models import News, SliderHomepage,PaymentMethod, Category


admin.site.register(News)
admin.site.register(SliderHomepage)
admin.site.register(PaymentMethod)
admin.site.register(Category)