from django.db import models

# Create your models here.
class tblDangKyHoc(models.Model):
    id = models.IntegerField(primary_key=True)
    khoa_hoc = models.CharField(max_length=264, default='')
    ho_ten = models.CharField(max_length=264, default='')
    dien_thoai = models.CharField(max_length=264, default='')
    email = models.EmailField()
    ngay_dang_ky = models.DateField()