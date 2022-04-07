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
]