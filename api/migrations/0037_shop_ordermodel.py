# Generated by Django 4.2.5 on 2024-03-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_delete_ordermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop_ordermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.TextField(null=True)),
                ('track_id', models.TextField(null=True)),
                ('quantity', models.TextField(null=True)),
                ('order_date', models.DateField(auto_now_add=True, null=True)),
                ('total_amount', models.TextField(null=True)),
                ('business_id', models.TextField(null=True)),
                ('shop_id', models.TextField(null=True)),
                ('product_id', models.TextField(null=True)),
            ],
        ),
    ]
