# Generated by Django 3.1.7 on 2021-05-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210521_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='photo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
