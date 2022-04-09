from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views import View
from django.contrib import messages
from django.views.generic import ListView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.contrib.auth.decorators import login_required
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
@login_required()
def profile(request):
    # customer = Customer.
    return render(request, 'app/profile.html')


def home(request):
  product = Product.objects.all()
  context= {'product':product}
  return render(request,'app/home.html',context)

def bidform(request):
  if request.method == 'POST':
    form = BidForm(request.POST,request.FILES)
    if form.is_valid():
      instance=form.instance.user = Customer.objects.get(user_id=request.user.id)
      instance=form.save()
      return redirect('/')
  else:
    form=BidForm()
  
  return render(request, 'app/bidform.html',{'form':form})

class ProductCreateView(CreateView):
  model = Product
  template_name = 'app/bidform.html'
  form_class = BidForm

  def form_valid(self, form):
    form.instance.user = Customer.objects.get(user_id=self.request.user.id)
    return super().form_valid(form)

class productDetailView(DetailView):
  model = Product
  template_name = 'app/product_detail.html'
  
def mypostitems(request,pk):
  customer = Customer.objects.get(user_id=request.user.id )
  product = Product.objects.filter(user=Customer.objects.get(user_id=request.user.id))
  return render(request, 'app/mypostitems.html',{'customer':customer,'product':product})
def bidamountform(request,pk):
  url=request.META.get('HTTP_REFERER')
  
  bid=Bid.objects.filter(product=pk)
  if request.method == 'POST':
    form = Bidamount(request.POST)
    if form.is_valid():
      instance=form.instance.product = Product.objects.get(pk=pk)
      instance = form.save(commit=False)
      form.instance.user = Customer.objects.get(user_id=request.user.id)
      instance.save()
      return redirect(url)
  else:
    form = Bidamount()
  return render(request,'app/bidamount.html',{'form':form,'bid':bid})

def bidamountdata(request):
  bid = Bid.objects.all()
  return render(request, 'app/bid.html',{'bid':bid})