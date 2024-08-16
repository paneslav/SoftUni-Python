# Generated by Django 5.0.4 on 2024-06-28 11:10

from django.db import migrations


def set_price(apps, schema_editor):
    device = apps.get_model('main_app', 'Smartphone')
    all_devices = device.objects.all()

    for device in all_devices:
        device.price = len(device.brand_name) * 120
        device.save()


def reverse_set_price(apps, schema_editor):
    device = apps.get_model('main_app', 'Smartphone')
    all_devices = device.objects.all()

    for device in all_devices:
        device.price = 0
        device.save()


def set_category(apps, schema_editor):
    device = apps.get_model('main_app', 'Smartphone')
    all_devices = device.objects.all()

    for device in all_devices:
        if device.price >= 750:
            device.category = 'Expensive'
        else:
            device.category = 'Cheap'
        device.save()


def reverse_set_category(apps, schema_editor):
    device = apps.get_model('main_app', 'Smartphone')
    all_devices = device.objects.all()

    for device in all_devices:
        device.category = 'No category'
        device.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_price, reverse_code=reverse_set_price),
        migrations.RunPython(set_category, reverse_code=reverse_set_category),
    ]