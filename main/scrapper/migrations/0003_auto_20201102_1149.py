# Generated by Django 3.1.2 on 2020-11-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0002_auto_20201102_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(max_length=2083),
        ),
    ]
