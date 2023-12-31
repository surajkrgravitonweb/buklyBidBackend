# Generated by Django 5.0 on 2024-01-01 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApi', '0006_bid_profilemodel_aadhar_profilemodel_pancard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApi.item')),
            ],
        ),
    ]
