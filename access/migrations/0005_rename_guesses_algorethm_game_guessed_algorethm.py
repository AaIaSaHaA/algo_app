# Generated by Django 4.0.5 on 2023-05-15 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_game_guesses_algorethm_game_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='guesses_algorethm',
            new_name='guessed_algorethm',
        ),
    ]