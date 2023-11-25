from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_view
from .form import LoginForm, MyPasswordResetFrom, MySetPasswordForm

urlpatterns = [
    path('', views.Index, name='home'),
    path('home/', views.Index, name='home'),
    path('best seller/<slug:val>', views.BestSeller.as_view(), name='bestseller'),
    path('offer/<slug:val>', views.OfferZone.as_view(), name='offer'),
    path('category/<slug:val>', views.CatrgoryView.as_view(), name="category"),
    path('details/<int:pk>', views.ProductDetails.as_view(), name='prodetail'),
    
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('show_cart', views.show_cart, name='show_cart'),
    
    path('checkout', views.checkout.as_view(), name='checkout'),
    path('paymentdone', views.paymentdone, name='paymentdone'),
    path('orders/', views.orders, name='orders'),
    
    path('search', views.search),
    
    # path('pluswishlist', views.plusWishlist),
    # path('minuswishlist', views.minusWishlist),
    
    path('buynow', views.buynow, name='buynow'),
    path('checkoutbuy', views.checkoutbuy.as_view(), name='checkoutbuy'),
    path('PaymentDone', views.PaymentDone, name='PaymentDone'),
    path('pluscart', views.plus_cart),
    path('minuscart', views.minus_cart),
    path('removecart', views.remove_cart), 
    path('registration/', views.RegistrationForm.as_view(), name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm),name='login'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>', views.UpdateAddress.as_view(), name='updateAddress'),
    path('addDel/<int:id>/',views.addDel, name='addDel'), 
    path('logout/', auth_view.LogoutView.as_view(next_page='home'), name='logout'),
    path('reset_password/', auth_view.PasswordResetView.as_view(template_name='password-reset.html',form_class=MyPasswordResetFrom), name='passwordReset'),
    path('reset_password/Done/', auth_view.PasswordResetDoneView.as_view(template_name='reset-done.html'), name='password_reset_done'),
    path('reset-password-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='reset-conformation.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='reset-complete.html'), name='password_reset_complete'),
]