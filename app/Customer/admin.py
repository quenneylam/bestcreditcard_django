from django.forms import *
from django.db.models import *
from .models import *
from django.contrib import admin
from .models import ThongTinKhachHang

# Register your forms here.
admin.site.register(ThongTinKhachHang)
