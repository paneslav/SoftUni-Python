# Generated by Django 5.0.4 on 2024-06-26 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_exercise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='is_favourite',
            new_name='is_favorite',
        ),
    ]