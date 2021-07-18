from django.db import models

# Create your models here.
class ThongTinKhachHang(models.Model):
    ma_KH = models.CharField(primary_key=True, max_length=20, unique=True)
    ho_ten = models.CharField(max_length=150, unique=True, blank=False, null=False)
    NAM = 'NAM'
    NU= 'NU'
    KHAC ='KHAC'
    GIOI_TINH =(
        (NAM, 'Nam'),
        (NU, 'Nữ'),
        (KHAC, 'Khác')
    )

    gioi_tinh = models.CharField(max_length=4, choices=GIOI_TINH, default=NAM)
    ngay_sinh = models.DateField()
    quoc_tinh = models.CharField(max_length=30, blank=False, null=False)
    so_cmnd_cccd_hc = models.CharField(max_length=30, blank=False, null=False)
    ngay_cap = models.DateField()
    dia_chi_thuong_tru = models.TextField()
    dia_chi_hien_tai = models.TextField()
    sdt = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    so_nguoi_phu_thuoc = models.PositiveIntegerField(default=0)
    #Trình độ học vấn
    TREN_DH = 'TDH'
    DAI_HOC = 'DH'
    CAO_DANG = 'CD'
    TRUNG_CAP = 'TC'
    KHAC = 'KH'
    TRINH_DO_HOC_VAN = (
        (TREN_DH, 'Trên đại học'),
        (DAI_HOC, 'Đại học'),
        (CAO_DANG, 'Cao đẳng'),
        (TRUNG_CAP, 'Trung cấp'),
        (KHAC, 'Khác'))
    trinh_do_hoc_van = models.CharField(max_length=3,choices=TRINH_DO_HOC_VAN,default=TREN_DH )

    #Loại nhà ở
    BIET_THU = 'BT'
    NHA_LIEN_KE = 'NLK'
    NHA_DAT = 'ND'
    CHUNG_CU = 'CC'
    LOAI_NHA_O = (
        (BIET_THU, 'Biệt thự'),
        (NHA_LIEN_KE, 'Nhà liền kề'),
        (NHA_DAT, 'Nhà đất'),
        (CHUNG_CU, 'Chung cư'),
        (KHAC, 'Khác'))
    Loai_nha_o = models.CharField(max_length=2, choices=LOAI_NHA_O, default=BIET_THU)

    #Hình thức sở hữu nhà

    NHA_RIENG = 'NR'
    NHA_DI_THUE ='NDT'
    NHA_THUE_MUA ='NTM'
    O_CHUNG_BO_ME='OCBM'
    NHA_MUA_TRA_GOP='NMTG'
    KHAC='KHAC'
    HINH_THUC_O_HUU_NHA =(
        (NHA_RIENG, 'Nhà riêng'),
        (NHA_DI_THUE, 'Nhà đi thuê'),
        (NHA_THUE_MUA, 'Nhà thuê mua'),
        (O_CHUNG_BO_ME,'Ở chung với bố mẹ(trừ trường hợp bô mẹ cũng đi thuê nhà)'),
        (NHA_MUA_TRA_GOP, 'Nhà mua trả chậm'),
        (KHAC, 'Khác')
    )
    hinh_thuc_so_huu_nha =models.CharField(max_length=4, choices=HINH_THUC_O_HUU_NHA, default=NHA_RIENG)


    #Tình trạng hôn nhân
    DOC_THAN = 'DT'
    DA_CO_GD = 'DCGD'
    LY_DI ='LD'
    GOA= 'G'
    LY_THAN ='LT'
    KHAC ='KH'
    TINH_TRANG_HON_NHAN = (
        (DOC_THAN, 'Độc thân'),
        (DA_CO_GD, 'Đã có gia đình'),
        (LY_DI, 'Ly dị'),
        (GOA, 'Goá'),
        (LY_THAN, 'Ly thân'),
        (KHAC, 'Khác'))
    tinh_trang_hon_nhan= models.CharField(max_length=4,choices=TINH_TRANG_HON_NHAN, default=DOC_THAN)
