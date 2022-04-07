from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views import View
# Create your views here.
def home(request):
  return render(request,'app/home.html',)
class CustomerRegistration(View):
  def get(self,request):
    form = CustomerRegistrationFrom()
    return render(request,'app/customerregistration.html',{'form':form})
  def post(self,request):
    form = CustomerRegistrationFrom(request.POST,request.FILES)
    if form.is_valid():
      messages.success(request,"Congratulations!!! Registered successfully Login Now")
      form.save()
      return redirect('login')
    return render(request, 'app/customerregistration.html',{'form':form})

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'app/login.html',context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/login')