# Generated by Django 2.0.7 on 2018-09-24 17:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_date_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='heure_msg',
            field=models.TextField(default=datetime.datetime(2018, 9, 24, 17, 59, 36, 376205, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_msg',
            field=models.DateField(default=datetime.datetime(2018, 9, 24, 17, 59, 36, 376205, tzinfo=utc)),
        ),
    ]
