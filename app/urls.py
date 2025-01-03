from django.urls import path
from django.conf import settings 
from app import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.forms import LoginForm, UserPasswordChangeForm, PasswordResetForm, PasswordResetConfirm

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('register/', views.CustomerRegistrationView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('contact/', views.contact, name='contact'),
    # URL for product details
    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('changepassword/' , auth_views.PasswordChangeView.as_view(template_name='changepassword.html', form_class=UserPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name="passwordchangedone.html"), name='passwordchangedone'),

    path('address/', views.address, name='address'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('pluscart/', views.plus_cart, name='plus-cart'),
    path('minuscart/', views.minus_cart, name='minus-cart'),
    path('removecart/', views.remove_cart, name='remove-cart'),
    path('orders/', views.orders, name='orders'),
    
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    
    # Password reset method
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=PasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=PasswordResetConfirm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
