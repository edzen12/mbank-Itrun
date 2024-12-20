from django.contrib import admin
from .models import News, SliderHomepage,PaymentMethod, Category, Partners


admin.site.register(News)
admin.site.register(SliderHomepage)
admin.site.register(PaymentMethod)
admin.site.register(Category)

@admin.register(Partners)
class PatnersAdmin(admin.ModelAdmin):
    list_display = ('title','phone1')