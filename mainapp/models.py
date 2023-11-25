from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICE = {
    ('poco', 'poco'),
    ('iphone', 'iphone'),
    ('redmi', 'redmi'),
    ('realme', 'realme'),
    ('samsung', 'samsung'),
}

BESTSELLER_CHOICE = {
    ('best', 'bestseller')
}

OFFERZONE_CHOICE = {
    ('offerzone', 'offer')
}

STATE_CHOICE = {
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Delhi', 'Delhi'),
    ('Puducherry', 'Puducherry')
}
STATUS_CHOICES = {
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancelled','Cancelled'),
    ('Pending','Pending'), 
}

class BestSellerFrontPage(models.Model):
    mobileImage = models.ImageField(upload_to = 'bestsellerfrontpage')
    mobileRating = models.CharField(max_length=10, null=True, blank=True)
    mobileName = models.CharField(max_length=150, null=True, blank=True)
    mobilePrice = models.IntegerField(null=True)
    mobileRam = models.CharField(max_length=200,null=True, blank=True)
    mobileDisplay = models.CharField(max_length=200,null=True, blank=True)
    mobileCamera = models.CharField(max_length=200,null=True, blank=True)
    mobileBattery = models.CharField(max_length=200,null=True, blank=True)
    mobileProcessor = models.CharField(max_length=200,null=True, blank=True)
    
    def __str__(self) :
        return self.mobileName
    
    

class OfferZoneFrontPage(models.Model):
    mobileImage = models.ImageField(upload_to = 'offerzonefrontpage')
    mobilePrice = models.IntegerField(null=True)
    mobileOfferPrice = models.IntegerField(null=True)
    
    def __str__(self) :
        return self.mobileName
    
    
      
class Products(models.Model):
    mobileImage = models.ImageField(upload_to = 'products')
    mobileImageSpec1 = models.ImageField(upload_to = 'products', null=True)
    mobileImageSpec2 = models.ImageField(upload_to = 'products', null=True)
    mobileImageSpec3 = models.ImageField(upload_to = 'products', null=True)
    mobileImageSpec4 = models.ImageField(upload_to = 'products', null=True)
    mobileImageSpec5 = models.ImageField(upload_to = 'products', null=True)
    mobileRating = models.CharField(max_length=10, null=True, blank=True)
    mobileName = models.CharField(max_length=150, null=True, blank=True)
    mobilePrice = models.IntegerField(null=True,blank=True)
    mobileOfferPrice = models.IntegerField(null=True,blank=True)
    mobileRam = models.CharField(max_length=200,null=True, blank=True)
    mobileDisplay = models.CharField(max_length=200,null=True, blank=True)
    mobileCamera = models.CharField(max_length=200,null=True, blank=True)
    mobileBattery = models.CharField(max_length=200,null=True, blank=True)
    mobileProcessor = models.CharField(max_length=200,null=True, blank=True)
    mobileCategory = models.CharField(choices=CATEGORY_CHOICE, max_length=10)
    mobileBestSeller = models.CharField(choices=BESTSELLER_CHOICE, max_length=10, null=True, blank=True)
    makeItOffer = models.CharField(choices=OFFERZONE_CHOICE, max_length=30, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Product'
        
    def __str__(self) :
        return self.mobileName


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    
    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name = 'Customers'
        verbose_name_plural = 'Customer'
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(default=0, null=True)
    
    # class Meta:
    #     verbose_name = 'Carts'
    #     verbose_name_plural = 'Cart'
    
    @property
    def TotalCost(self):
        return self.quantity * self.product.mobileOfferPrice
    
    
    
# =============== buy now ===================

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Order'
    
    @property
    def get_total_cost(self):
        return self.quantity * self.product.mobileOfferPrice




class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField()
    razorpay_order_id =models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_status = models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_id = models.CharField(max_length=100,null=True,blank=True)
    paid = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Payments'
        verbose_name_plural = 'Payment'
    
    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    
    class Meta:
        verbose_name = 'OrderPlaceds'
        verbose_name_plural = 'OrderPlaced'
    
    @property
    def total_cost(self):
        return self.quantity * self.product.mobileOfferPrice
    

class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    

