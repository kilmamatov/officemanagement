# Generated by Django 4.1.3 on 2023-03-24 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_userprofile_nickname_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='userprofile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.userprofile', verbose_name='Забранировано'),
            preserve_default=False,
        ),
    ]
