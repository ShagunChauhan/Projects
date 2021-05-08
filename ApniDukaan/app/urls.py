from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, CurrentPasswordChangeForm, CurrentPasswordResetForm, CurrentSetPasswordForm

urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.checkout, name='checkout'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('buy/', views.buy_now, name='buy-now'),
    # path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=CurrentPasswordChangeForm, success_url='/changepassworddone/'), name='changepassword'),
    path('changepassworddone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/changepassworddone.html'), name='changepassworddone'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    # path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=CurrentPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=CurrentSetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
