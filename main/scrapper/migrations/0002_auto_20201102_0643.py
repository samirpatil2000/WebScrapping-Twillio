# Generated by Django 3.1.2 on 2020-11-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='news',
            name='published',
        ),
        migrations.RemoveField(
            model_name='news',
            name='source',
        ),
        migrations.RemoveField(
            model_name='news',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default='This is the content'),
        ),
    ]
