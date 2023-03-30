# Generated by Django 4.1.3 on 2023-03-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Кабинет', 'verbose_name_plural': 'Кабинеты'},
        ),
        migrations.AlterField(
            model_name='room',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Конец брони'),
        ),
        migrations.AlterField(
            model_name='room',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Начало брони'),
        ),
    ]
