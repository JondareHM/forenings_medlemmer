# Generated by Django 2.2.2 on 2019-06-27 14:35

from django.db import migrations



def move_person(apps, schema_editor):
    Person = apps.get_model('members', 'Person')
    Address = apps.get_model('members', 'Address')
    for person in Person.objects.all():
        if person.address_moved == False:
            if person.dawa_id in Address.objects.values_list('dawa_id', flat=True):
                address_obj = Address.objects.get(dawa_id=person.dawa_id)
                person.postal_address = address_obj
                person.address_moved = True
                person.save()
            else:
                # Address not already in Address table. Create new record
                new_address = Address.objects.create(
                    streetname = person.streetname,
                    housenumber = person.housenumber,
                    floor = person.floor,
                    door = person.door,
                    city = person.city,
                    zipcode = person.zipcode,
                    municipality = person.municipality,
                    placename = person.placename,
                    longitude = person.longitude,
                    latitude = person.latitude,
                    dawa_id = person.dawa_id,
                    address_invalid = person.address_invalid
                )
                person.address_moved = True
                person.save()


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20190627_1635'),
    ]

    operations = [
    ]