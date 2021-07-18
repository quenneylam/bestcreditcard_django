from django.shortcuts import render
from django.http import HttpResponse
import json, urllib.request
from .models import Product
# Create your views here.

def getList(request):
    pro_list = Product.objects.order_by('name')
    result_list = list(pro_list.values('name', 'price', 'description', 'image'))
    return HttpResponse(json.dumps(result_list, ensure_ascii=False).encode('utf8'))

def ket_noi_api_laySP(request):
    DEFAULT_ENCODING = 'utf-8'
    url = 'http://127.0.0.1:8000/product_api/'
    urlResponse = urllib.request.urlopen(url)

    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding =urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING

    data = json.loads(urlResponse.read().decode(encoding))
    return HttpResponse(data)

