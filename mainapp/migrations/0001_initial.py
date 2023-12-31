# Generated by Django 4.2 on 2023-04-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_image', models.ImageField(upload_to='bestseller')),
                ('mobileName', models.CharField(blank=True, max_length=150, null=True)),
                ('mobilePrice', models.CharField(blank=True, max_length=50, null=True)),
                ('mobileRam', models.CharField(max_length=200)),
                ('mobileDisplay', models.CharField(max_length=200)),
                ('mobileCamera', models.CharField(max_length=200)),
                ('mobileBattery', models.CharField(max_length=200)),
                ('mobileProcessor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BestSellerFrontPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileImage', models.ImageField(upload_to='bestsellerfrontpage')),
                ('mobileName', models.CharField(blank=True, max_length=150, null=True)),
                ('mobilePrice', models.CharField(blank=True, max_length=50, null=True)),
                ('mobileRam', models.CharField(max_length=200)),
                ('mobileDisplay', models.CharField(max_length=200)),
                ('mobileCamera', models.CharField(max_length=200)),
                ('mobileBattery', models.CharField(max_length=200)),
                ('mobileProcessor', models.CharField(max_length=200)),
            ],
        ),
    ]
