from django.http import HttpResponse
import json
from .models import Product
def product_service(request):
    pro_list = Product.obj.order_by('name')
