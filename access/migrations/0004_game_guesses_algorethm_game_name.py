# Generated by Django 4.0.5 on 2023-05-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='guesses_algorethm',
            field=models.CharField(default='Not enough to guess', max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
