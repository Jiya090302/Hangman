# Generated by Django 4.1.7 on 2023-04-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangmanGame', '0004_alter_hangman_game_guessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangman_game',
            name='difficulty',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]