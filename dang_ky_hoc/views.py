from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.parsers import JSONParser
from .models import tblDangKyHoc
from .serializers import DangKyHocserializer
# Create your views here.
@csrf_exempt
def dang_ky_hoc_list(request):
    if request.method =='GET':
        _tblDangKyHoc = tblDangKyHoc.objects.all()
        serializer = DangKyHocserializer(_tblDangKyHoc, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DangKyHocserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def dang_ky_hoc_detail(request, pk):
     try:
         _tblDangKyHoc =tblDangKyHoc.objects.get(pk =pk)
     except tblDangKyHoc.DoesNotExist:
         return HttpResponse(status=404)

     if request.method == 'GET':
         serializer = DangKyHocserializer(_tblDangKyHoc)
         return JsonResponse (serializer.data)

     elif request.method ==  'PUT':
         data = JSONParser().parse(request)
         serializer = DangKyHocserializer(_tblDangKyHoc, data= data)
         if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data)
         return JsonResponse(serializer.errors, status=400)
     elif request.method =='DELETTE':
         _tblDangKyHoc.delete()
         return  HttpResponse(status= 204)

