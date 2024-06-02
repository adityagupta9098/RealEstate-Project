# Generated by Django 4.1.3 on 2024-05-25 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=45)),
                ('last_name', models.CharField(default='', max_length=45)),
                ('email_id', models.EmailField(default='', max_length=45, unique=True)),
                ('mobile_no', models.CharField(default='', max_length=12)),
                ('role', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(default='', max_length=200)),
                ('area_sq_feet', models.DecimalField(decimal_places=2, max_digits=10)),
                ('num_bedrooms', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('hospitals_nearby', models.TextField()),
                ('colleges_nearby', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='RealEstateapp.user')),
            ],
        ),
    ]
