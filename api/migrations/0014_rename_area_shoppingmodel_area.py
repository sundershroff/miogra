# Generated by Django 4.2.5 on 2024-02-13 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_d_originalmodel_area_d_originalmodel_door_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingmodel',
            old_name='Area',
            new_name='area',
        ),
    ]