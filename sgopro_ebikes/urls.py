"""sgopro_ebikes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sgoapp_ebikes import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth import views as auth_views
from sgoapp_ebikes.views import payment_status,coffee_payment
from django.conf.urls.static import static
from django.conf import settings
from sgoapp_ebikes.views import edit_cust_profile_view

admin.site.site_header = "SGO Admin"
admin.site.site_title = "SGO Admin Portal"
admin.site.index_title = "Welcome to SGO Portal"
admin.site.site_url = ""
app_name = 'account'
from django.urls import reverse_lazy
from sgoapp_ebikes.views import manage_dealers
from sgoapp_ebikes.views import dealerUpdate
from sgoapp_ebikes.views import dealerRemove
from sgoapp_ebikes.views import manage_user,dealernewvistors,edit_dealer_profile_view,userUpdate,adminnewvistors,userRemove,manage_cust,custRemove,custUpdate,BikeRead,BikeReadfull,dealerBikeReadfull,dealerBikeRead
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('home', views.home_view,name='home'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),

    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='customerlogin.html'), name='customerlogin'),
    path('customer-home', views.customer_home_view, name='customer-home'),
    path('dealersignup', views.dealer_signup_view),
    path('dealerlogin', LoginView.as_view(template_name='dealerlogin.html'), name='dealerlogin'),
    path('dealer-home', views.dealer_home_view, name='dealer-home'),

    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # profiles........
    path('my-cust-profile', views.my_cust_profile_view, name='my-cust-profile'),
    path('my-admin-profile', views.my_admin_profile_view, name='my-admin-profile'),
    path('my-dealer-profile', views.my_dealer_profile_view, name='my-dealer-profile'),
    path('my-cust-edit-profile/', edit_cust_profile_view.as_view(), name='my-cust-edit-profile'),
    path('my-admin-edit-profile', views.edit_admin_profile_view, name='my-admin-edit-profile'),
    path('my-dealer-edit-profile', edit_dealer_profile_view.as_view(), name='my-dealer-edit-profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    # path('password/', views.change_password, name='change_password'),
    path('password/', PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password1/', PasswordChangeView.as_view(template_name='registration/change_password1.html')),
    path('password2/', PasswordChangeView.as_view(template_name='registration/change_password2.html')),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/success_password.html'), name='password_change_done'),


    #customer-dash...
    path('customer-battery/',views.cust_battery),
    path('customer-kms/',views.cust_km_view),
    path('customer-estimation/',views.cust_Estimation),
    path('customer-vlocation/',views.vehloc),
    path('customer-diagnostics/',views.diagnostics),
    path('customer-speedo/',views.speedo),
    path('customer-estimate_kms/',views.estimate_kms),
    path('dealer-new/',views.dealer_new),
    path('user-new/',views.user_new),
    path('user-dealer-new/',views.user_dealer_new),
    # path('manage-dealers/',views.manage_dealers),
    path('manage-dealers/', manage_dealers.as_view(),name='listdealers'),
    path('dupdate/<int:pk>/', dealerUpdate.as_view()),
    path('ddelete/<int:pk>/', dealerRemove.as_view()),

    path('manage-user/', manage_user.as_view(), name='listusers'),
    path('uupdate/<int:pk>/', userUpdate.as_view()),
    path('udelete/<int:pk>/', userRemove.as_view()),

    path('manage-customers/', manage_cust.as_view(), name='listcust'),
    path('custupdate/<int:pk>/', custUpdate.as_view()),
    path('custdelete/<int:pk>/', custRemove.as_view()),

    path('lockunlock/', views.LockUnlock, name='lockunlock'),
    path('lockunlock1/', views.lockunlock_afterlogin, name='lockunlock1'),

    # path('bookbike/', coffee_payment, name='coffee-payment'),
    # path('payment-status', payment_status, name='payment-status'),

    path('vistors', views.vistors, name='vistors'),
    path('vistorss', views.vistorss, name='vistorss'),
    path('', include('sgoapp_ebikes.urls')),
    path('bikepayments/', BikeRead.as_view(), name='listbikes'),
    path('bikesales/', BikeReadfull.as_view(), name='listbikessales'),


    path('dealerbikesales/', dealerBikeReadfull.as_view(), name='listdaelerbikessales'),
    path('dealerbikepayments/', dealerBikeRead.as_view(), name='listdaelerbikes'),
    path('newadminvisitor/', adminnewvistors.as_view()),
    path('newdealervisitor/', dealernewvistors.as_view()),

]
