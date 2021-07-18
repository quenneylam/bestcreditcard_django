from django.shortcuts import render
from Products import *
from Products.models import CardInformation

# Create your views here.


def home_view(request):
    return render(request, 'bestcreditcard/home.html')


def card_detail_view(request, pk):
    card_list_ltv = CardInformation.objects.order_by('name_card')
    list_cart = CardInformation.objects.first()
    card_detail = CardInformation.objects.get(pk=pk)
    context = {
        'card_detail': card_detail,
        'card': card_list_ltv,
        'list_cart': list_cart
    }
    return render(request, 'Products/product_detail.html', context)

