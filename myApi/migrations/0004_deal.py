# Generated by Django 5.0 on 2023-12-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApi', '0003_carmodel_profilemodel_servicesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_no', models.CharField(max_length=100, unique=True)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=200)),
                ('new_state', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('deal_date', models.DateField()),
                ('customer_name', models.CharField(max_length=200)),
                ('registration_no', models.CharField(blank=True, max_length=100, null=True)),
                ('rc_available', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3)),
                ('repo_date', models.DateField()),
                ('segment', models.CharField(max_length=100)),
                ('parked_at', models.TextField()),
                ('yard_city', models.CharField(max_length=100)),
                ('valuation_amount', models.FloatField()),
                ('valuation_report_link', models.URLField(max_length=500)),
                ('manufacturing_year', models.IntegerField()),
                ('base_rate', models.FloatField()),
            ],
        ),
    ]
