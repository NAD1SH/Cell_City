from django.shortcuts import render, redirect
from django.views import View
from .models import *
from . form import customRegistrationForm, CustomerProfile
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
import razorpay
from django.conf import settings


client=razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
# Create your views here.

def Index(request):
    totalitem = len(Cart.objects.filter(user=request.user))
    bestProduct = {
        'bestseller' : BestSellerFrontPage.objects.all(),
        'item' : totalitem
    }
    return render(request, 'index.html', bestProduct)

class BestSeller(View):
    def get(self, request, val):
        product = Products.objects.filter(mobileBestSeller=val)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
        return render(request, 'bestSeller.html', locals())

def LoginPage(request):
    return render(request, 'login.html')


class CatrgoryView(View):
    def get(self, request, val):
        product = Products.objects.filter(mobileCategory=val)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))    
        return render(request, 'category.html', locals())

class OfferZone(View):
    def get(seft, request, val):
        product = Products.objects.filter(makeItOffer=val)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
        return render(request, 'offer.html', locals())
    

class ProductDetails(View):
    def get(self, request, pk):
        product = Products.objects.get(pk=pk)   
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
        # Wishlist = wishlist.objects.filter(Q(product=product) & Q(user=request.user))
          
        return render(request, 'productdetails.html', locals())
    
    
class RegistrationForm(View):
    def get(self, request):
        form = customRegistrationForm()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
        return render(request, 'register.html', locals())
    def post(self, request):
        form = customRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations ! User Register successfully')
            return redirect('login')
        else:
            messages.warning(request, 'Invalid Input Data') 
        return render(request, 'register.html', locals())
    
class UserProfile(View):
    def get(self, request):
        form = CustomerProfile()
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user = request.user))
        return render(request, 'profile.html', locals())
    def post(self, request):
        form = CustomerProfile(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations Profile Save Successfully')
               
        else:
            messages.warning(request, '\Invalid Input Data')
        return render(request, 'addressPage.html', locals())
    
    
def address(request):
    add = Customer.objects.filter(user = request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))
    return render(request, 'addressPage.html', locals())
    

class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfile(instance=add)
        return render(request, 'Update-address.html', locals())
    def post(self, request, pk):
        form = CustomerProfile(request.POST) 
        if form.is_valid():
            add = Customer.objects.get(pk=pk)   
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,'Congratulations ! Proifle Update Successfully')
        else:
            messages.warning(request, 'Invalid Input Data')
        return render(request, 'profile .html', locals())
    
    
def addDel(request, id):
      add_del = Customer.objects.get(id=id)
      add_del.delete()
      return redirect('address')
      

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id') 
    products = Products.objects.get(id=product_id)
    if Cart.objects.filter(user=request.user, product=products):
        return redirect('/show_cart')
    else:
        Cart(user=user, product=products).save()
        return redirect('/show_cart')


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for i in cart:
        value = i.quantity * i.product.mobilePrice
        amount = amount + value
    totalamount = amount + 40
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user))  
    return render(request, 'addToCart.html', locals())



class checkout(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for i in cart_items:
            value = i.quantity * i.product.mobileOfferPrice
            famount = famount + value
        totalamount = famount + 40
        
        razoramount = int(totalamount * 100)
        data = {'amount' : razoramount, 'currency' : 'INR', 'receipt' : 'order_rcptid_11'}
        payment_response = client.order.create(data=data)
        print(payment_response)  
        # {'id': 'order_LmgOhxYglukQLw', 'entity': 'order', 'amount': 1303900, 'amount_paid': 0, 'amount_due': 1303900, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1683442853}   
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user = user,
                amount = totalamount,
                razorpay_order_id = order_id,
                razorpay_payment_status = order_status
            )   
            payment.save()
        return render(request, 'checkout.html', locals())


    
def paymentdone(request):
    
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        payment_id = request.POST.get('payment_id')
        cust_id = request.POST.get('cust_id')
        print('payment done:',order_id, 'pid : ', payment_id)
        user = request.user
        customer = Customer.objects.get(id=cust_id)
        payment = Payment.objects.get(razorpay_order_id = order_id)
        payment.paid = True
        payment.razorpay_payment_id = payment_id
        payment.save()
        cart = Cart.objects.filter(user = user)
        for i in cart:
            OrderPlaced(user=user, product=i.product, quantity=i.quantity, payment=payment).save()
            i.delete()
    return redirect('orders')
    # return HttpResponse("Payment Successful")

        
#==========================================



def buynow(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    products = Products.objects.get(id=product_id)
    if Order is not None:
        del_pro = Order.objects.all()
        del_pro.delete()
        Order(user=user, product=products).save()
    else:
       Order(user=user, product=products).save()
    return redirect('/checkoutbuy')

class checkoutbuy(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Order.objects.filter(user=user)
        famount = 0
        for i in cart_items:
            value = 1 * i.product.mobileOfferPrice
            famount = famount + value
        totalamount = famount + 40
        
        razoramount = int(totalamount * 100)
        data = {'amount' : razoramount, 'currency' : 'INR', 'receipt' : 'order_rcptid_11'}
        payment_response = client.order.create(data=data)
        print(payment_response)  
        # {'id': 'order_LmgOhxYglukQLw', 'entity': 'order', 'amount': 1303900, 'amount_paid': 0, 'amount_due': 1303900, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1683442853}   
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user = user,
                amount = totalamount,
                razorpay_order_id = order_id,
                razorpay_payment_status = order_status
            )   
            payment.save()
        return render(request, 'checkoutbuy.html', locals())
    
def PaymentDone(request):
    
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        payment_id = request.POST.get('payment_id')
        cust_id = request.POST.get('cust_id')
        print('payment done:',order_id, 'pid : ', payment_id)
        user = request.user
        customer = Customer.objects.get(id=cust_id)
        payment = Payment.objects.get(razorpay_order_id = order_id)
        payment.paid = True
        payment.razorpay_payment_id = payment_id
        payment.save()
        cart = Order.objects.filter(user = user)
        for i in cart:
            OrderPlaced(user=user, product=i.product, quantity=i.quantity, payment=payment).save()
            i.delete()
    return redirect('orders')

# ======================================================



def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for i in cart:
            value = i.quantity * i.product.mobileOfferPrice
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity' : i.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }
        return JsonResponse(data)
    
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for i in cart:
            value = i.quantity * i.product.mobileOfferPrice
            amount = amount + value
        totalamount = amount + 40
        data = {
            'quantity' : i.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user).first()
        amount = 0
        print(cart)
        if cart != None:
            print('cart not empty')
            for i in cart:
                value = i.quantity * i.product.mobileOfferPrice
                amount = amount + value
                totalamount = amount + 40
                data = {
                    'quantity' : i.quantity,
                    'amount' : amount,
                    'totalamount' : totalamount,
                    "cart" : True
                }
        else:
            print('cart empty')
            data = {
                'cart' : False
            }
            return JsonResponse(data)
        return JsonResponse(data)
    

def orders (request) :
    order_placed = Payment.objects.filter(user=request.user)
    return render (request,'orders.html',locals())

      
def search(request) : 
    query = request.GET['search']
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user = request.user)) 
    product = Products.objects.filter(Q(mobileName__icontains=query)) 
    return render (request,'search.html',locals()) 



def plusWishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Products.objects.get(id=prod_id)
        user = request.user
        wishlist(user=user, product=product).save()
        data = {
            'massage' : 'Wishlist Added Successfully'
        }
        return JsonResponse(data)
    

def minusWishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Products.objects.get(id=prod_id)
        user = request.user
        wishlist.objects.filter(user=user, product=product).delete() 
        data = {
            'massage' : 'Wishlist Added Successfully'
        }
        return JsonResponse(data)
        