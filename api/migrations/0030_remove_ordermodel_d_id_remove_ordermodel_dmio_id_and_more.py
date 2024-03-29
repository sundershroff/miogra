# Generated by Django 4.2.5 on 2024-02-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_ordermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='dmio_id',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='food_id',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='fresh_id',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='jewel_id',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='pharm_id',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='shop_id',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='order_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='order_id',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='track_id',
            field=models.TextField(null=True),
        ),
    ]
