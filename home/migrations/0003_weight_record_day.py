# Generated by Django 3.1.1 on 2020-09-28 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200926_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='weight',
            name='record_day',
            field=models.DateField(default=datetime.date.today, verbose_name='记录时间'),
        ),
    ]