from django.db import models


class SliderHomepage(models.Model):
    title = models.CharField(max_length=100)
    little_text = models.CharField(max_length=100)
    img = models.ImageField(upload_to='sliders')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Слайдер'
        verbose_name = 'слайдер'


class News(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(upload_to='service', null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'услуга'


class PaymentMethod(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='payMethod')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Способы оплаты'
        verbose_name = 'способ оплаты'


class Category(models.Model):
    title = models.CharField(max_length=40, verbose_name="Название категории")
    img = models.CharField(max_length=255, verbose_name="cсылка на фото")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категория'

