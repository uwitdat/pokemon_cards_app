# Generated by Django 3.1.7 on 2021-05-21 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20210521_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]