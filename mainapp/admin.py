from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(BestSellerFrontPage)
admin.site.register(OfferZoneFrontPage)
admin.site.register(Products)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']
    
@admin.register(Cart)
class CartModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'product','image', 'quantity', 'price']
    
@admin.register(Order)
class OrderModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']
    
@admin.register(Payment)
class paymentModel(admin.ModelAdmin):
    list_display =['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid']
    
@admin.register(OrderPlaced)
class orderPlacedModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']
    
@admin.register(wishlist)
class wishlistModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']
    