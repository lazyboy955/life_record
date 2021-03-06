# Generated by Django 3.1.1 on 2020-09-26 01:16

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('username', models.CharField(max_length=200, verbose_name='用户名')),
                ('weight', models.FloatField(verbose_name='体重')),
                ('remark', models.CharField(default='', max_length=300, verbose_name='备注')),
                ('period_of_time', models.PositiveSmallIntegerField(choices=[(0, 'day'), (1, 'night')], default=home.models.get_default_period_of_time, verbose_name='时间段')),
            ],
            options={
                'verbose_name': '体重表',
                'verbose_name_plural': '体重表',
                'db_table': 'weight',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
