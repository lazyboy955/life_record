# Generated by Django 3.0.7 on 2020-06-23 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_weight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.AlterModelOptions(
            name='weight',
            options={'verbose_name': '体重表', 'verbose_name_plural': '体重表'},
        ),
        migrations.AlterModelTable(
            name='weight',
            table='weight',
        ),
    ]
