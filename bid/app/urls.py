from django.urls import path
from . import views
from .views import *
from .form import *
from django.contrib.auth import views as auth_views
urlpatterns=[

  path('registration/',views.CustomerRegistration.as_view(),name="registration"),
  path('login/',views.login_request, name='login'),
  path('logout/',views.logout_view, name='logout'),
  path('',views.home, name='home'),
  path('bidform/', views.bidform, name="bidform"),
  path('items/<str:pk>/', views.mypostitems, name="items"),
  path('bidamount/<int:pk>/', views.bidamountform, name="bidamount"),
  path('bidamountdata/', views.bidamountdata, name="bidamountdata"),
  path('bidforms/', views.ProductCreateView.as_view(), name="bidforms"),
  path('product-detail/<int:pk>/', views.productDetailView.as_view(), name="product-detail"),
]