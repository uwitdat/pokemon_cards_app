# Generated by Django 3.1.7 on 2021-05-19 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210519_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='none', max_length=150),
        ),
    ]
