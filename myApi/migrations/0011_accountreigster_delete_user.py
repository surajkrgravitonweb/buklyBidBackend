# Generated by Django 4.2.9 on 2024-01-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApi', '0010_remove_user_image_alter_user_is_deleted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountReigster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
