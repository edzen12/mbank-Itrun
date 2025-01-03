# Generated by Django 4.2.17 on 2024-12-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_category_options_alter_category_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('img', models.CharField(max_length=255, verbose_name='Ссылка на лого')),
                ('website', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на сайт')),
                ('address1', models.CharField(max_length=105, verbose_name='Адрес №1')),
                ('address2', models.CharField(blank=True, max_length=105, null=True, verbose_name='Адрес №2')),
                ('phone1', models.CharField(help_text='996770770770', max_length=12, verbose_name='Телефон №1')),
                ('phone2', models.CharField(blank=True, help_text='996770770770', max_length=12, null=True, verbose_name='Телефон №2')),
                ('category', models.ManyToManyField(to='news.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
    ]
