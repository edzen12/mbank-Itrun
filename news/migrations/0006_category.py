# Generated by Django 4.2.17 on 2024-12-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_paymentmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название категории')),
                ('img', models.ImageField(upload_to='category')),
            ],
            options={
                'verbose_name': 'Категория',
            },
        ),
    ]
