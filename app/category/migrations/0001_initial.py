# Generated by Django 2.0.3 on 2018-03-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '图片分类',
                'verbose_name_plural': '图片分类',
                'db_table': 'db_category',
            },
        ),
    ]
