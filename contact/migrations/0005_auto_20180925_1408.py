# Generated by Django 2.0.7 on 2018-09-25 12:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20180925_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_msg',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='heure_msg',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
