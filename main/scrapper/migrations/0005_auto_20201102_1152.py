# Generated by Django 3.1.2 on 2020-11-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0004_auto_20201102_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(blank=True, default='No Link', max_length=2083, null=True),
        ),
    ]