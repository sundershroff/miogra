# Generated by Django 4.2.5 on 2024-02-27 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_d_originalproductsmodel_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.d_originalmodel')),
                ('dmio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dailymio_model')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.foodmodel')),
                ('fresh_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.freshcutsmodel')),
                ('jewel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jewellerymodel')),
                ('pharm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pharmacy_model')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shoppingmodel')),
            ],
        ),
    ]
