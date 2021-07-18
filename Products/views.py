# Products views
from django.shortcuts import render
from .models import CardInformation

# Create your views here.


def base_product(request):
    return render(request, 'Products/base_product.html')


def shopping(request):
    card_list_ltv = CardInformation.objects.order_by('name_card')
    list_cart = CardInformation.objects.all()
    # filter(danh_muc_1='Shopping').filter(danh_muc_2='Shopping')
    context = {
        'card': card_list_ltv,
        'list_cart': list_cart
        }
    return render(request, 'Products/shopping.html', context)


def tra_gop_0(request):
    card_list_ltv = CardInformation.objects.order_by('name_card')
    list_cart = CardInformation.objects.all()
    # filter(danh_muc_1='Trả góp 0%').filter(danh_muc_2='Shopping')

    context = {
        'card': card_list_ltv,
        'list_cart': list_cart}
    return render(request, 'Products/tra-gop-0.html', context)


def dam_bay(request):
    card_list_ltv = CardInformation.objects.order_by('name_card')
    list_cart = CardInformation.objects.all()
    #  filter(danh_muc_1='Dặm bay').filter(danh_muc_2='Dặm bay')

    context = {
        'card': card_list_ltv,
        'list_cart': list_cart}
    return render(request, 'Products/dam-bay.html', context)


def di_lai(request):
    card_list_ltv = CardInformation.objects.order_by('name_card')
    list_cart = CardInformation.objects.all()
    # filter(danh_muc_1='Đi lại') | CardInformation.objects.filter(danh_muc_2='Đi lại')

    context = {
        'card': card_list_ltv,
        'list_cart': list_cart}
    return render(request, 'Products/di-lai.html', context)


def thanh_toan_online(request):
    card_list_ltv = CardInformation.objects.order_by('name_card')
    list_cart = CardInformation.objects.all()
    # filter(danh_muc_1='Thanh toán online').filter(danh_muc_2='Thanh toán online')

    context = {
        'card': card_list_ltv,
        'list_cart': list_cart}
    return render(request, 'Products/thanh-toan-online.html', context)


def bao_hiem(request):
    card_list_ltv = CardInformation.objects.order_by('name_card')
    list_cart = CardInformation.objects.all()
    # filter(danh_muc_1='Bảo hiểm').filter(danh_muc_2='Bảo hiểm')

    context = {
        'card': card_list_ltv,
        'list_cart': list_cart}
    return render(request, "Products/bao-hiem.html", context)


def the_mien_phi(request):
    card_list_ltv = CardInformation.objects.order_by('name_card')
    list_cart = CardInformation.objects.all()
    # filter(danh_muc_1='Thẻ miễn phí').filter(danh_muc_2='Thẻ miễn phí')
    context = {
        'card': card_list_ltv,
        'list_cart': list_cart}
    return render(request, 'Products/the-mien-phi.html', context)


def card_detail_view(request, pk):
    card_detail = CardInformation.objects.get(pk=pk)

    context = {
        'card_detail': card_detail,
    }
    return render(request, 'Products/product_detail.html', context)

