from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from .models import *
import razorpay
from .forms import CoffeePaymentForm
from django.views.decorators.csrf import csrf_exempt
from . import forms,models
from .forms import PasswordChangingForm
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from . import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from . import forms,models
from sgoapp_ebikes.models import cust
from .forms import PasswordChangingForm
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from . import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomerForm, CustomerUserForm
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from .models import *
import razorpay
from .forms import CoffeePaymentForm
from django.views.decorators.csrf import csrf_exempt
from . import forms,models
from .forms import PasswordChangingForm
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from . import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from . import forms,models
from sgoapp_ebikes.models import cust
from .forms import PasswordChangingForm
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from . import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import CustomerForm, CustomerUserForm
from django.contrib import messages
from .forms import dealerUserForm, dealerForm

from .forms import dealerUserForm, dealerForm
def home_view(request):
    return render(request,'index.html')




def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.username = user.email
            # username=user.username
            # def username_exists(username):

            if User.objects.filter(username=user.username).exists():

                return render(request,'validation/custuser.html')
            else:
                user.save()
                customer = customerForm.save(commit=False)
                customer.user = user
                customer.save()
                my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
                my_customer_group[0].user_set.add(user)
                return HttpResponseRedirect('customerlogin')

    return render(request,'customersignup.html',context=mydict)
#-----------for checking user iscustomer
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


def dealer_signup_view(request):
    userForm=forms.dealerUserForm()
    dealerForm=forms.dealerForm()
    mydict={'userForm':userForm,'dealerForm':dealerForm}
    if request.method=='POST':
        userForm=forms.dealerUserForm(request.POST)
        dealerForm=forms.dealerForm(request.POST,request.FILES)
        if userForm.is_valid() and dealerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.username = user.email
            if User.objects.filter(username=user.username).exists():

                return render(request, 'validation/dealeruser.html')
            else:
                user.save()
                customer = dealerForm.save(commit=False)
                customer.user = user
                customer.save()
                my_dealer_group = Group.objects.get_or_create(name='dealer')
                my_dealer_group[0].user_set.add(user)
                return HttpResponseRedirect('dealerlogin')

    return render(request,'dealersignup.html',context=mydict)

#-----------for checking user isdealer
def is_dealer(user):
    return user.groups.filter(name='dealer').exists()

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request):
    # bike = models.bike.objects.filter(customer_id = request.user.id)
    # return render(request, 'customerdash.html', {'bike': bike})
    return render(request, 'UserDashboard/index.html')

@login_required(login_url='dealerlogin')
@user_passes_test(is_dealer)
def dealer_home_view(request):
    # for cards on dashboard
    customercount = models.cust.objects.all().count()
    bikecount = models.bookbike.objects.all().count()
    mydict = {
        'customercount': customercount,
        'bikecount': bikecount,
    }
    return render(request,'DealerDashbaord/dealerindex.html', context=mydict)

@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
    customercount = models.cust.objects.all().count()
    dealercount = models.dealer.objects.all().count()
    bikecount = models.bookbike.objects.all().count()
    mydict = {
        'customercount': customercount,
        'dealercount': dealercount,
        'bikecount': bikecount,
    }
    return render(request,'Admin Dashbaord/adminindex.html',context=mydict)


def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-home')
    if is_dealer(request.user):
        return redirect('dealer-home')
    else:
        return redirect('admin-dashboard')



@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def my_cust_profile_view(request):
    customer=models.cust.objects.get(user_id=request.user.id)
    # user1=models.User.objects.get(user_id=request.user.id)
    return render(request,'my_cust_profile.html',{'customer':customer})

class edit_cust_profile_view(LoginRequiredMixin, TemplateView):
    user_form = CustomerUserForm
    profile_form = CustomerForm
    template_name = 'edit_cust_profile.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = CustomerUserForm(post_data, instance=request.user)
        profile_form = CustomerForm(post_data, file_data, instance=request.user.cust)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('my-cust-profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
# @login_required(login_url='customerlogin')
# @user_passes_test(is_customer)
# def edit_cust_profile_view(request):
#     customer=models.cust.objects.get(user_id=request.user.id)
#     user=models.User.objects.get(id=customer.user_id)
#     userForm=forms.CustomerUserForm(instance=user)
#     customerForm=forms.CustomerForm(request.FILES,instance=customer)
#     mydict={'userForm':userForm,'customerForm':customerForm}
#     if request.method=='POST':
#         userForm=forms.CustomerUserForm(request.POST,instance=user)
#         customerForm=forms.CustomerForm(request.POST,instance=customer)
#         if userForm.is_valid() and customerForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.username = user.email
#             user.save()
#             customerForm.save()
#             return HttpResponseRedirect('my-cust-profile')
#     return render(request,'edit_cust_profile.html',context=mydict)

@login_required(login_url='dealerlogin')
@user_passes_test(is_dealer)
def my_dealer_profile_view(request):
    dealer=models.dealer.objects.get(user_id=request.user.id)
    return render(request,'my_dealer_profile.html',{'dealer':dealer})


class edit_dealer_profile_view(LoginRequiredMixin, TemplateView):
    user_form = dealerUserForm
    profile_form = dealerForm
    template_name = 'edit_dealer_profile.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = dealerUserForm(post_data, instance=request.user)
        profile_form = dealerForm(post_data, file_data, instance=request.user.dealer)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('my-dealer-profile'))

        context = self.get_context_data(
                                        user_form =user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# @login_required(login_url='dealerlogin')
# @user_passes_test(is_dealer)
# def edit_dealer_profile_view(request):
#     dealer=models.dealer.objects.get(user_id=request.user.id)
#     user=models.User.objects.get(id=dealer.user_id)
#     userForm=forms.dealerUserForm(instance=user)
#     dealerForm=forms.dealerForm(request.FILES,instance=dealer)
#     mydict={'userForm':userForm,'dealerForm':dealerForm}
#     if request.method=='POST':
#         userForm=forms.dealerUserForm(request.POST,instance=user)
#         dealerForm=forms.dealerForm(request.POST,instance=dealer)
#         if userForm.is_valid() and dealerForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.username = user.email
#             user.save()
#             dealerForm.save()
#             return HttpResponseRedirect('my-dealer-profile')
#     return render(request,'edit_dealer_profile.html',context=mydict)

class PasswordsChangeView(PasswordChangeView):
      from_class=PasswordChangingForm
      success_url = reverse_lazy('home')

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def cust_battery(request):
    status = models.Battery_status.objects.filter(customer_id=request.user.id)
    return render(request,'UserDashboard/battey.html',{'status': status})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def cust_km_view(request):
    bike = kilometers.objects.filter(customer_id=request.user.id)
    return render(request,'UserDashboard/kms.html',{'bike':bike})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def cust_Estimation(request):
    recharge =Recharge.objects.filter(customer_id=request.user.id)
    return render(request,"UserDashboard/recharge.html",{'recharge':recharge})



@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def diagnostics(request):
    bike = models.bike.objects.filter(customer_id = request.user.id)
    return render(request, 'UserDashboard/invoice.html', {'bike': bike})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def speedo(request):
    recharge =Speedometer.objects.filter(customer_id=request.user.id)
    return render(request,'UserDashboard/speedo.html',{'speed':recharge})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def estimate_kms(request):
    recharge =estimatekms.objects.filter(customer_id=request.user.id)
    return render(request,'UserDashboard/maps.html',{'recharge':recharge})

@login_required(login_url='adminlogin')
def my_admin_profile_view(request):
    # user = models.User.objects.get(user_id=request.user.id)
    return render(request, 'Admin Dashbaord/adminprofileview.html')

@login_required(login_url='adminlogin')
def edit_admin_profile_view(request):
    user=models.User.objects.get(id=request.user.id)
    userForm=forms.AdminUserForm(instance=user)
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.AdminUserForm(request.POST,instance=user)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.username = user.email
            user.save()
            return HttpResponseRedirect('afterlogin')
    return render(request,'edit_admin_profile.html',context=mydict)

@login_required(login_url='adminlogin')
def dealer_new(request):
    userForm=forms.dealerUserForm()
    dealerForm=forms.dealerForm()
    mydict={'userForm':userForm,'dealerForm':dealerForm}
    if request.method=='POST':
        userForm=forms.dealerUserForm(request.POST)
        dealerForm=forms.dealerForm(request.POST,request.FILES)
        if userForm.is_valid() and dealerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.username = user.email
            if User.objects.filter(username=user.username).exists():

                return render(request, 'validation/admindealeruser.html')
            else:
                user.save()
                customer = dealerForm.save(commit=False)
                customer.user = user
                customer.save()
                my_dealer_group = Group.objects.get_or_create(name='dealer')
                my_dealer_group[0].user_set.add(user)
                return HttpResponseRedirect('afterlogin')

    return render(request,'Admin Dashbaord/adminnewdealer.html',context=mydict)

@login_required(login_url='adminlogin')
def user_new(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.username = user.email
            if User.objects.filter(username=user.username).exists():

                return render(request, 'validation/admincustuser.html')
            else:
                user.save()
                customer = customerForm.save(commit=False)
                customer.user = user
                customer.save()
                my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
                my_customer_group[0].user_set.add(user)
                return HttpResponseRedirect('afterlogin')

    return render(request,'Admin Dashbaord/adminnewcustomer.html',context=mydict)

@login_required(login_url='dealerlogin')
@user_passes_test(is_dealer)
def user_dealer_new(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.username = user.email
            if User.objects.filter(username=user.username).exists():

                return render(request, 'validation/dealercustuser.html')
            else:
                user.save()
                customer = customerForm.save(commit=False)
                customer.user = user
                customer.save()
                my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
                my_customer_group[0].user_set.add(user)
                return HttpResponseRedirect('afterlogin')

    return render(request,'DealerDashbaord/dealernewcustomer.html',context=mydict)

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def vehloc(request):
    return render(request,'UserDashboard/vloc.html')


class manage_dealers(ListView):
    model = dealer
    template_name = 'Admin Dashbaord/adminmanagedealer.html'

class dealerUpdate(UpdateView):
    model = dealer
    fields = '__all__'
    template_name = "Admin Dashbaord/dealerupdate.html"

    def get_success_url(self):
        return reverse('listdealers')

class dealerRemove(DeleteView):
    model = dealer
    template_name = "Admin Dashbaord/dealer_confirm_delete.html"
    success_url = reverse_lazy('listdealers')




class manage_user(ListView):
    model = cust
    template_name = 'Admin Dashbaord/adminmanagecustomer.html'

class userUpdate(UpdateView):
    model = cust
    fields = '__all__'
    template_name = "Admin Dashbaord/userupdate.html"

    def get_success_url(self):
        return reverse('listusers')

class userRemove(DeleteView):
    model = cust
    template_name = "Admin Dashbaord/user_confirm_delete.html"
    success_url = reverse_lazy('listusers')

class manage_cust(ListView):
    model = cust
    template_name = 'DealerDashbaord/dealermanagecustomer.html'

class custUpdate(UpdateView):
    model = cust
    fields = '__all__'
    template_name = "DealerDashbaord/custupdate.html"

    def get_success_url(self):
        return reverse('listcust')


class custRemove(DeleteView):
    model = cust
    template_name = "DealerDashbaord/cust_confirm_delete.html"
    success_url = reverse_lazy('listcust')

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def LockUnlock(request):
    lockunlock = models.LockUnlock.objects.all()
    # lockunlock =LockUnlock.objects.filter(customer_id=request.user.id)

    return render(request, 'UserDashboard/unlock.html', {'lockunlock': lockunlock})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def lockunlock_afterlogin(request):
    return render(request, 'UserDashboard/lockunlock-pin.html')

@login_required(login_url='adminlogin')
def vistors(request):
    return render(request,'Admin Dashbaord/adminvisitor.html')


@login_required(login_url='dealerlogin')
@user_passes_test(is_dealer)
def vistorss(request):
    return render(request,'DealerDashbaord/dealervisitor.html')


@login_required(login_url='adminlogin')
def coffee_payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        bikename = request.POST.get('bikename')
        amount = int(request.POST.get('amount')) * 100
        country = request.POST.get('country')
        # shop_name = request.POST.get('shop_name')
        # dealer_name = request.POST.get('dealer_name')
        # dealer_shopname = request.POST.get('dealer_shopname')
        # create Razorpay clientss
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))

        # create order
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            cold_coffee = bookbike(
                name=name,
                number=number,
                email=email,
                address=address,
                pincode=pincode,
                state=state,
                country=country,
                # dealer_name_id=dealer_name,
                # dealer_shopname=dealer_shopname,
                bikename=bikename,
                amount=amount,
                order_id=order_id
            )
            cold_coffee.save()
            response_payment['name'] = name

            form = CoffeePaymentForm(request.POST or None)
            return render(request, 'coffee_payment1.html', {'form': form, 'payment': response_payment})

    form = CoffeePaymentForm()
    return render(request, 'Admin Dashbaord/coffee_payment.html', {'form': form})





@login_required(login_url='dealerlogin')
@user_passes_test(is_dealer)
def coffee_payment1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        bikename = request.POST.get('bikename')
        amount = int(request.POST.get('amount')) * 100

        # create Razorpay clientss
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))

        # create order
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            cold_coffee = bookbike(
                name=name,
                number=number,
                email=email,
                address=address,
                pincode=pincode,
                state=state,
                bikename=bikename,
                amount=amount,
                order_id=order_id
            )
            cold_coffee.save()
            response_payment['name'] = name

            form = CoffeePaymentForm(request.POST or None)
            return render(request, 'dealercoffee_payment1.html', {'form': form, 'payment': response_payment})

    form = CoffeePaymentForm()
    return render(request, 'DealerDashbaord/dealercoffee_payment.html', {'form': form})


def payment_status(request):

    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        cold_coffee = bookbike.objects.get(order_id=response['razorpay_order_id'])
        cold_coffee.razorpay_payment_id = response['razorpay_payment_id']
        cold_coffee.paid = True
        cold_coffee.save()
        return render(request, 'payment_status.html', {'status': True})
    except:
        return render(request, 'payment_status.html', {'status': False})


class BikeRead(ListView):
    model = bookbike
    template_name = 'Admin Dashbaord/adminbikesales.html'


class BikeReadfull(ListView):
    model = bookbike
    template_name = 'Admin Dashbaord/adminbikesaleshistory.html'



class dealerBikeReadfull(ListView):
    model = bookbike
    template_name = 'DealerDashbaord/dealerbikesales.html'


class dealerBikeRead(ListView):
    model = bookbike
    template_name = 'DealerDashbaord/dealerpaymenthistory.html'


class adminnewvistors(CreateView):
    model=adminvisit
    fields = ('first_name','last_name','gender','mobile_no','address','pincode','dealer_name','bikename','purpose')
    template_name = 'Admin Dashbaord/adminnewvisitors.html'

    def get_success_url(self):
        return reverse('vistors')

class dealernewvistors(CreateView):
    model=adminvisit
    fields = ('first_name','last_name','gender','mobile_no','address','pincode','dealer_name','bikename','purpose')
    template_name = 'DealerDashbaord/dealernewvisitors.html'

    def get_success_url(self):
        return reverse('vistorss')



@login_required(login_url='adminlogin')
def vistors(request):
    visit=models.adminvisit.objects.all()
    visitcount = models.adminvisit.objects.all().count()

    return render(request,'Admin Dashbaord/adminvisitor.html',{'visit':visit,'visitcount':visitcount})


@login_required(login_url='dealerlogin')
@user_passes_test(is_dealer)
def vistorss(request):
    visit = models.adminvisit.objects.filter(dealer_name_id=request.user.dealer.id)
    visitcount = models.adminvisit.objects.filter(dealer_name_id=request.user.dealer.id).count()

    # return render(request, 'newdealervisitorhistory.html', {'forms': forms, 'visitorcount': visitorcount})
    # visit = models.dealervisit.objects.all()
    # # visit =dealervisit.objects.filter(id=request.id)
    # visitcount = models.dealervisit.objects.all().count()
    return render(request,'DealerDashbaord/dealervisitor.html',{'visit':visit,'visitcount':visitcount})

