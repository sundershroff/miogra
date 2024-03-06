# Generated by Django 4.2.5 on 2024-02-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_ordermodel_d_id_ordermodel_dmio_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='d_originalmodel',
            name='region',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dailymio_model',
            name='region',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='region',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='freshcutsmodel',
            name='region',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_model',
            name='region',
            field=models.TextField(null=True),
        ),
    ]