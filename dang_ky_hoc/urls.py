from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

#from product_service import views
from . import views

urlpatterns = [
path('dang_ky_hoc_list/<int: pk>', views.dang_ky_hoc_list, name='dang-ky-hoc-list'),

]