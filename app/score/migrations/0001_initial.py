# Generated by Django 2.0.3 on 2018-03-15 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='')),
                ('image', models.OneToOneField(on_delete='CASCADE', to='image.Image', verbose_name='图片')),
            ],
            options={
                'verbose_name': '图片评分',
                'verbose_name_plural': '图片评分',
                'db_table': 'db_source',
            },
        ),
        migrations.CreateModel(
            name='UserRateing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='')),
                ('point', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='得分')),
                ('evaluation_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评分时间')),
                ('images', models.ForeignKey(on_delete='CASCADE', to='image.Image', verbose_name='评价的图片')),
                ('users', models.ManyToManyField(to='user.User', verbose_name='评价的用户')),
            ],
            options={
                'verbose_name': '用户评分',
                'verbose_name_plural': '用户评分',
                'db_table': 'db_source_rateing',
            },
        ),
    ]
