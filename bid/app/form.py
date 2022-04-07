
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.db import transaction

class CustomerRegistrationFrom(UserCreationForm):
  password1 = forms.CharField(label='Password',widget=forms.
  PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label='Comfrim Password',widget=forms.
  PasswordInput(attrs={'class':'form-control'}))
  email = forms.CharField(required=True,widget=forms.
  EmailInput(attrs={'class':'form-control'}))

  class Meta(UserCreationForm.Meta):
    model=User
    fields = ['username','email','password1','password2',]
    labels ={'email': 'Email',}
    widgets  = {'username':forms.TextInput(attrs=
    {'class':"form-control"})}

  @transaction.atomic
  def save(self):
    user = super().save(commit=False)
    user.is_customer = True
    
    user.save()
    customer = Customer.objects.create(user=user)
    customer.email = self.cleaned_data.get('email')
    customer.save()
    return user
    