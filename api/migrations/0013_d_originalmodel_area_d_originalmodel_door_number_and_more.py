# Generated by Django 4.2.5 on 2024-02-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_d_originalmodel_pickup_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='d_originalmodel',
            name='Area',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='d_originalmodel',
            name='door_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='d_originalmodel',
            name='street_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dailymio_model',
            name='Area',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dailymio_model',
            name='door_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dailymio_model',
            name='street_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='Area',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='door_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='street_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='freshcutsmodel',
            name='Area',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='freshcutsmodel',
            name='door_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='freshcutsmodel',
            name='street_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jewellerymodel',
            name='Area',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jewellerymodel',
            name='door_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jewellerymodel',
            name='street_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_model',
            name='Area',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_model',
            name='door_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_model',
            name='street_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shoppingmodel',
            name='Area',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shoppingmodel',
            name='door_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='shoppingmodel',
            name='street_name',
            field=models.TextField(null=True),
        ),
    ]
