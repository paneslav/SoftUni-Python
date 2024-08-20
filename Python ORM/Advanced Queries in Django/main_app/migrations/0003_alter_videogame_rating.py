# Generated by Django 5.0.4 on 2024-08-19 22:25

import main_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_videogame_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[main_app.validators.RangeValidator(0, 10, message='The rating must be between 0.0 and 10.0')]),
        ),
    ]