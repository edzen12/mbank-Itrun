# Generated by Django 4.2.17 on 2024-12-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.CharField(max_length=255, verbose_name='cсылка на фото'),
        ),
    ]
