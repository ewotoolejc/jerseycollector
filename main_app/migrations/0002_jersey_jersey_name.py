# Generated by Django 4.2 on 2023-04-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jersey',
            name='jersey_name',
            field=models.CharField(default='My New Jersey', max_length=50),
        ),
    ]
