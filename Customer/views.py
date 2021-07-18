from django.shortcuts import render
from . import forms
from .models import ThongTinKhachHang

# Create your views here.

def FormRegisterCustomer_view(request):
    form = forms.FormRegisterCustomer(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'Customer/form-phat-hanh-the.html', context)
