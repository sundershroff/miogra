# Generated by Django 4.2.5 on 2024-02-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessmodel',
            name='created_date',
            field=models.TextField(null=True),
        ),
    ]
