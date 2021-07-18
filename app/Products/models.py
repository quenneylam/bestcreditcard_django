from django.db import models
from django.urls import reverse
# Create your models here.


class CardInformation(models.Model):
    # tổ chưc thẻ
    VISA = 'CV'
    MASTERCARD = 'CM'
    JCB = 'JCB'
    UNIONPAY = 'UP'
    AMEX = 'AMEX'
    CREDIT = (
        (VISA, 'Visa'),
        (MASTERCARD, 'MasterCard'),
        (JCB, 'JCB'),
        (UNIONPAY, 'UnionPay'),
        (AMEX, 'American Express'),
    )
    # Danh mục
    SHOPPING = 'shopping'
    TRA_GOP_0 = 'tra_gop_0'
    DAM_BAY = 'dam_bay'
    DI_LAI = 'di_lai'
    BAO_HIEM = 'bao_hiem'
    THANH_TOAN_ONLINE = 'thanh_toan_online'
    THE_MIEN_PHI = 'the_mien_phi'

    DANH_MUC = (
        (SHOPPING, 'Shopping'),
        (TRA_GOP_0, 'Trả góp 0%'),
        (DAM_BAY, 'Dặm bay'),
        (DI_LAI, 'Đi lại'),
        (BAO_HIEM, 'Bảo hiểm'),
        (THANH_TOAN_ONLINE, 'Thanh toán online'),
        (THE_MIEN_PHI, 'Thẻ miễn phí'),

    )

    # thônng tin chung
    ID_card = models.CharField(primary_key=True, max_length=100, unique=True, blank=False, null=False)
    name_card = models.CharField(max_length=150, unique=True, blank=False, null=False)
    danh_muc_1 = models.CharField(max_length=20, choices=DANH_MUC, blank=False, null=False)
    danh_muc_2 = models.CharField(max_length=20, choices=DANH_MUC, blank=False, null=False)
    ngan_hang = models.CharField(max_length=200, blank=False, null=False)
    to_chuc_the = models.CharField(max_length=4, choices=CREDIT, blank=False, null=False)
    yeu_cau_thu_nhap = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=False)
    han_muc = models.CharField(max_length=50, blank=False, null=False)
    phi_thuong_nien = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False)
    lai_suat = models.FloatField(blank=False, null=False)
    so_ngay_mien_lai = models.PositiveIntegerField(blank=False, null=False)
    phi_phat_hanh = models.DecimalField(max_digits=7, decimal_places=0, blank=False, null=False )
    hoan_tien_trung_binh = models.FloatField(blank=True, null=True)
    hoan_tien_cao_nhat = models.FloatField(blank=True, null=True)
    hinh_anh_sp = models.ImageField(blank=True, null=True)
    # phí lưu ý
    phi_ung_tien_mat=models.CharField(max_length=100, blank=True, null=True)
    phi_giao_dich_ngoai_te = models.CharField(max_length=100, blank=True, null=True)
    phi_thanh_toan_cham = models.CharField(max_length=100, blank=True, null=True)
    so_tien_toi_thieu_phai_tra_moi_thang = models.DecimalField(max_digits=10, decimal_places=0, )
    tich_luy_uu_dai_bang = models.CharField(max_length=100, blank=True, null=True)

    # ưu đãi sủ dụng thẻ
    Wireless_payment = models.BooleanField(blank=True, null=True)
    tra_gop_lai_suat_0 = models.TextField(blank=True, null=True)
    chuong_trinh_KH_than_thiet =models.TextField(blank=True, null=True)
    uu_dai_di_lai = models.TextField(blank=True, null=True)
    hoan_tien_khi_tra_phi_bao_hiem = models.TextField(blank=True, null=True)
    bao_hiem_du_lich = models.TextField(blank=True, null=True)
    dich_vu_ho_tro_du_lich = models.TextField(blank=True, null=True)
    mien_phong_cho_san_bay = models.CharField(max_length=10, blank=True, null=True)
    so_lan_mien_phong_cho_san_bay_trong_nam = models. PositiveIntegerField(default=0)
    so_nguoi_duoc_mien_vao_phong_cho = models. PositiveIntegerField(default=0)
    khuyen_mai = models.TextField(blank=True, null=True)
    thu_tuc_phat_hanh_va_dieu_kien = models.TextField(blank=True, null=True)
    bieu_phi = models.URLField(max_length=200)

    def __str__(self):
        return self.name_card

    def get_absolute_url(self):
        return reverse('card_detail', args=[self.pk])


class Partner(models.Model):
    id_doi_tac = models.CharField(primary_key=True, max_length=10, unique=True, blank=False, null=False)
    ten_doi_tac = models.CharField(max_length=50, unique=True, blank=False, null=False)
    link = models.URLField(max_length=100)
    mo_ta_uu_dai = models.TextField()

    def __str__(self):
        return self.ten_doi_tac


class PartnerToProduct(models.Model):
    id_doi_tac = models.ForeignKey(Partner, on_delete=models.CASCADE)
    ID_card = models.ForeignKey(CardInformation, on_delete=models.CASCADE)






