# Generated by Django 4.1.3 on 2024-05-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstateapp', '0003_alter_user_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.CharField(default='', max_length=45),
        ),
    ]
