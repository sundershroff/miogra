# Generated by Django 4.2.5 on 2024-02-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_businessmodel_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='d_originalmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_id', models.TextField()),
                ('seller_name', models.TextField()),
                ('business_name', models.TextField()),
                ('pan_number', models.TextField()),
                ('gst', models.TextField()),
                ('contact', models.TextField()),
                ('alternate_contact', models.TextField()),
                ('pin_number', models.TextField()),
                ('pickup_location', models.TextField()),
                ('fssa', models.TextField()),
                ('pin_your_location', models.TextField()),
                ('name', models.TextField()),
                ('account_number', models.TextField()),
                ('ifsc_code', models.TextField()),
                ('upi_id', models.TextField()),
                ('gpay_number', models.TextField()),
                ('aadhar', models.TextField()),
                ('pan_file', models.TextField()),
                ('profile', models.TextField()),
                ('bank_passbook', models.TextField()),
                ('gst_file', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='dailymio_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_id', models.TextField()),
                ('seller_name', models.TextField()),
                ('business_name', models.TextField()),
                ('pan_number', models.TextField()),
                ('gst', models.TextField()),
                ('contact', models.TextField()),
                ('alternate_contact', models.TextField()),
                ('pin_number', models.TextField()),
                ('pickup_location', models.TextField()),
                ('fssa', models.TextField()),
                ('pin_your_location', models.TextField()),
                ('name', models.TextField()),
                ('account_number', models.TextField()),
                ('ifsc_code', models.TextField()),
                ('upi_id', models.TextField()),
                ('gpay_number', models.TextField()),
                ('aadhar', models.TextField()),
                ('pan_file', models.TextField()),
                ('profile', models.TextField()),
                ('bank_passbook', models.TextField()),
                ('gst_file', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='foodmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_id', models.TextField()),
                ('seller_name', models.TextField()),
                ('business_name', models.TextField()),
                ('pan_number', models.TextField()),
                ('gst', models.TextField()),
                ('contact', models.TextField()),
                ('alternate_contact', models.TextField()),
                ('pin_number', models.TextField()),
                ('pickup_location', models.TextField()),
                ('fssa', models.TextField()),
                ('pin_your_location', models.TextField()),
                ('name', models.TextField()),
                ('account_number', models.TextField()),
                ('ifsc_code', models.TextField()),
                ('upi_id', models.TextField()),
                ('gpay_number', models.TextField()),
                ('aadhar', models.TextField()),
                ('pan_file', models.TextField()),
                ('profile', models.TextField()),
                ('bank_passbook', models.TextField()),
                ('gst_file', models.TextField()),
                ('date', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='freshcutsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_id', models.TextField()),
                ('seller_name', models.TextField()),
                ('business_name', models.TextField()),
                ('pan_number', models.TextField()),
                ('gst', models.TextField()),
                ('contact', models.TextField()),
                ('alternate_contact', models.TextField()),
                ('pin_number', models.TextField()),
                ('pickup_location', models.TextField()),
                ('fssa', models.TextField()),
                ('pin_your_location', models.TextField()),
                ('name', models.TextField()),
                ('account_number', models.TextField()),
                ('ifsc_code', models.TextField()),
                ('upi_id', models.TextField()),
                ('gpay_number', models.TextField()),
                ('aadhar', models.TextField()),
                ('pan_file', models.TextField()),
                ('profile', models.TextField()),
                ('bank_passbook', models.TextField()),
                ('gst_file', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='jewellerymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_id', models.TextField()),
                ('seller_name', models.TextField()),
                ('business_name', models.TextField()),
                ('pan_number', models.TextField()),
                ('gst', models.TextField()),
                ('contact', models.TextField()),
                ('alternate_contact', models.TextField()),
                ('pin_number', models.TextField()),
                ('pickup_location', models.TextField()),
                ('pin_your_location', models.TextField()),
                ('name', models.TextField()),
                ('account_number', models.TextField()),
                ('ifsc_code', models.TextField()),
                ('upi_id', models.TextField()),
                ('gpay_number', models.TextField()),
                ('aadhar', models.TextField()),
                ('pan_file', models.TextField()),
                ('profile', models.TextField()),
                ('bank_passbook', models.TextField()),
                ('gst_file', models.TextField()),
                ('date', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacy_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_id', models.TextField()),
                ('seller_name', models.TextField()),
                ('business_name', models.TextField()),
                ('pan_number', models.TextField()),
                ('gst', models.TextField()),
                ('contact', models.TextField()),
                ('alternate_contact', models.TextField()),
                ('pin_number', models.TextField()),
                ('pickup_location', models.TextField()),
                ('fssa', models.TextField()),
                ('pin_your_location', models.TextField()),
                ('name', models.TextField()),
                ('account_number', models.TextField()),
                ('ifsc_code', models.TextField()),
                ('upi_id', models.TextField()),
                ('gpay_number', models.TextField()),
                ('aadhar', models.TextField()),
                ('pan_file', models.TextField()),
                ('profile', models.TextField()),
                ('bank_passbook', models.TextField()),
                ('gst_file', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='shoppingmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_id', models.TextField()),
                ('seller_name', models.TextField()),
                ('business_name', models.TextField()),
                ('pan_number', models.TextField()),
                ('gst', models.TextField()),
                ('contact', models.TextField()),
                ('alternate_contact', models.TextField()),
                ('pin_number', models.TextField()),
                ('pickup_location', models.TextField()),
                ('pin_your_location', models.TextField()),
                ('name', models.TextField()),
                ('account_number', models.TextField()),
                ('ifsc_code', models.TextField()),
                ('upi_id', models.TextField()),
                ('gpay_number', models.TextField()),
                ('aadhar', models.TextField()),
                ('pan_file', models.TextField()),
                ('profile', models.TextField()),
                ('bank_passbook', models.TextField()),
                ('gst_file', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='used_produtsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.TextField()),
                ('pan_file', models.TextField()),
                ('profile', models.TextField()),
                ('bank_passbook', models.TextField()),
                ('date', models.TextField()),
            ],
        ),
    ]