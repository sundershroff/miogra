# Generated by Django 4.2.5 on 2024-02-09 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_dailymio_model_dmio_id_used_produtsmodel_business_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailymio_model',
            name='fresh_id',
        ),
    ]