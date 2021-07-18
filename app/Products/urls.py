# Products.urls

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('danh-muc-product/', views.base_product, name='dm0'),
    path('shopping/', views.shopping, name='dm1'),
    path('tra-gop-0/', views.tra_gop_0, name='dm2'),
    path('dam-bay/', views.dam_bay, name='dm3'),
    path('di-lai/', views.di_lai, name='dm4'),
    path('bao-hiem/', views.bao_hiem, name='dm5'),
    path('thanh-toan-online/', views.thanh_toan_online, name='dm6'),
    path('the-mien-phi/', views.the_mien_phi, name='dm7'),
    path('chi-tiet/<int:pk>/', views.card_detail_view, name='card_detail'),
]
