#Customer.urls

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('form-phat-hanh-the/', views.FormRegisterCustomer_view, name='form_register_customer'),




 ]



