from django import forms
from django.contrib.auth.models import User
from . import models
from .models import bookbike

from django.forms import ModelForm
from  django.contrib.auth.forms import PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import validators
# from sgoapp_ebikes.validators import validate_email
from sgoapp_ebikes.validators import validate_email


class AdminUserForm(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput(),

        }
class CustomerUserForm(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }



        
class CustomerForm(ModelForm):
    class Meta:
        model=models.cust
        fields=['pincode','address','mobile','profile_pic','state','country','gender']

class dealerUserForm(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email']
        widgets = {
        'password': forms.PasswordInput()
        }

class dealerForm(ModelForm):
    class Meta:
        model=models.dealer
        fields=['pincode','address','mobile','profile_pic1','shop_name','gender','shop_address','dealer_type','state','country']

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')


class CoffeePaymentForm(forms.ModelForm):
    class Meta:
        model = bookbike
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'number',
            'email',
            'address',
            'pincode',
            'state',
            'country',
            # 'dealer_name',
            'bikename',
            'amount',
            Submit('submit', 'Buy', css_class='button white btn-block btn-primary')
        )
