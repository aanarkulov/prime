# Generated by Django 2.0.4 on 2018-04-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='title_en',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='title_ky',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='title_ru',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
