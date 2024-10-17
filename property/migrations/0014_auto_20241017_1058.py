from django.db import migrations


def link_owners_with_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )
        owner.owned_apartments.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20241017_0014'),
    ]

    operations = [
        migrations.RunPython(link_owners_with_flats, reverse_code=migrations.RunPython.noop),
    ]
