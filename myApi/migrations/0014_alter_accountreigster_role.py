# Generated by Django 5.0.1 on 2024-01-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApi', '0013_accountreigster_role_alter_accountreigster_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountreigster',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (3, 'User')], default=3, null=True),
        ),
    ]