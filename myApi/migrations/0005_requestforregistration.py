# Generated by Django 4.0.6 on 2024-01-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApi', '0004_bid_deal_item_premiumpayment_carmodel_auction_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestForRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('youAre', models.CharField(max_length=200)),
            ],
        ),
    ]