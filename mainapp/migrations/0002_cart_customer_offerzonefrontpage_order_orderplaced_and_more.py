# Generated by Django 4.2 on 2023-05-06 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=12)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Gujarat', 'Gujarat'), ('Assam', 'Assam'), ('Uttarakhand', 'Uttarakhand'), ('Puducherry', 'Puducherry'), ('Delhi', 'Delhi'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Goa', 'Goa'), ('Kerala', 'Kerala'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Bihar', 'Bihar'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Haryana', 'Haryana'), ('Karnataka', 'Karnataka'), ('Tamil Nadu', 'Tamil Nadu')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customers',
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='OfferZoneFrontPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileImage', models.ImageField(upload_to='offerzonefrontpage')),
                ('mobileName', models.CharField(blank=True, max_length=150, null=True)),
                ('mobilePrice', models.IntegerField(null=True)),
                ('mobileOfferPrice', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Orders',
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Cancelled', 'Cancelled'), ('On the Way', 'On the Way'), ('Delivered', 'Delivered')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer')),
            ],
            options={
                'verbose_name': 'OrderPlaceds',
                'verbose_name_plural': 'OrderPlaced',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payments',
                'verbose_name_plural': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileImage', models.ImageField(upload_to='products')),
                ('mobileImageSpec1', models.ImageField(null=True, upload_to='products')),
                ('mobileImageSpec2', models.ImageField(null=True, upload_to='products')),
                ('mobileImageSpec3', models.ImageField(null=True, upload_to='products')),
                ('mobileImageSpec4', models.ImageField(null=True, upload_to='products')),
                ('mobileImageSpec5', models.ImageField(null=True, upload_to='products')),
                ('mobileRating', models.CharField(blank=True, max_length=10, null=True)),
                ('mobileName', models.CharField(blank=True, max_length=150, null=True)),
                ('mobilePrice', models.IntegerField(blank=True, null=True)),
                ('mobileOfferPrice', models.IntegerField(blank=True, null=True)),
                ('mobileRam', models.CharField(blank=True, max_length=200, null=True)),
                ('mobileDisplay', models.CharField(blank=True, max_length=200, null=True)),
                ('mobileCamera', models.CharField(blank=True, max_length=200, null=True)),
                ('mobileBattery', models.CharField(blank=True, max_length=200, null=True)),
                ('mobileProcessor', models.CharField(blank=True, max_length=200, null=True)),
                ('mobileCategory', models.CharField(choices=[('poco', 'poco'), ('iphone', 'iphone'), ('samsung', 'samsung'), ('realme', 'realme'), ('redmi', 'redmi')], max_length=10)),
                ('mobileBestSeller', models.CharField(blank=True, choices=[('best', 'bestseller')], max_length=10, null=True)),
                ('makeItOffer', models.CharField(blank=True, choices=[('offerzone', 'offer')], max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.DeleteModel(
            name='BestSeller',
        ),
        migrations.AddField(
            model_name='bestsellerfrontpage',
            name='mobileRating',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bestsellerfrontpage',
            name='mobileBattery',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bestsellerfrontpage',
            name='mobileCamera',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bestsellerfrontpage',
            name='mobileDisplay',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bestsellerfrontpage',
            name='mobilePrice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bestsellerfrontpage',
            name='mobileProcessor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bestsellerfrontpage',
            name='mobileRam',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='payment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mainapp.payment'),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.products'),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.products'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.products'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
