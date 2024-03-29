# Generated by Django 4.2.5 on 2024-02-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_remove_d_originalmodel_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='d_originalproductsmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='dmio_dairymodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='dmio_eggsmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='dmio_fishmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='dmio_fruitsmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='dmio_grocerymodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='dmio_meatmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='dmio_vegitablesmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_bakerymodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_beefmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_biriyanimodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_burgermodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_cakemodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_chickenbiriyanimodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_chinesemodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_firedchickenmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_icecreammodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_mealsmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_pizzamodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_teacoffemodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='food_tiffenmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_beefmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_chickenmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_choppedvegmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_combomodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_dryfishmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_eggmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_fishseafoodmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_meatmasalamodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_muttonmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_pondfishmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='fresh_prawnsmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='jewel_goldmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='jewel_silvermodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_allopathicmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_ayurvedicmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_herbaldrinksmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_siddhamodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy_unanimodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_appliancesmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_autoaccessoriesmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_booksmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_electronicsmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_fashionmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_furnituremodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_groceriesmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_healthcaremodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_kitchenmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_mobilemodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_personalcaremodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_petsuppliesmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_sportsmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='shop_toysmodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
