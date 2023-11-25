# Generated by Django 4.2.1 on 2023-05-08 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_cart_customer_offerzonefrontpage_order_orderplaced_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Puducherry', 'Puducherry'), ('Haryana', 'Haryana'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Delhi', 'Delhi'), ('Bihar', 'Bihar'), ('Gujarat', 'Gujarat'), ('Uttarakhand', 'Uttarakhand'), ('Tamil Nadu', 'Tamil Nadu'), ('Goa', 'Goa'), ('Kerala', 'Kerala'), ('Assam', 'Assam'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Karnataka', 'Karnataka')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('On the Way', 'On the Way'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='mobileCategory',
            field=models.CharField(choices=[('iphone', 'iphone'), ('realme', 'realme'), ('samsung', 'samsung'), ('poco', 'poco'), ('redmi', 'redmi')], max_length=10),
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]