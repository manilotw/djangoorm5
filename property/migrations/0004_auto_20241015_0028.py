# Generated by Django 2.2.24 on 2024-10-14 21:28

from django.db import migrations


def set_new_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    
    for flat in Flat.objects.all():
        if flat.construction_year < 2015:
            flat.new_building = False
        else:
            flat.new_building = True
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_buildings)
    ]

