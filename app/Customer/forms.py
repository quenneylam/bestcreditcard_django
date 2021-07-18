
from django import forms
from .models import ThongTinKhachHang


class FormRegisterCustomer(forms.ModelForm):

    ma_KH = forms.CharField(label='Mã Khách hàng/ ID ', max_length=20,)
    ho_ten = forms.CharField(label='Họ và tên/ Full name  ', max_length=150)
    NAM = 'NAM'
    NU = 'NU'
    KHAC = 'KHAC'
    GIOI_TINH = (
        (NAM, 'Nam/Male'),
        (NU, 'Nữ/Female'),
        (KHAC, 'Khác/Other')
    )

    gioi_tinh = forms.ChoiceField(label='Giới tính/ Gender  ', choices=GIOI_TINH, initial='NAM')
    ngay_sinh = forms.DateField(label='Ngày sinh/ Day of birth  ', )
    quoc_tinh = forms.CharField(label='Quốc tịch/ ', max_length=30)
    so_cmnd_cccd_hc = forms.CharField(label='CMND/Số căn cước/Hộ chiếu/Passport', max_length=30)
    ngay_cap = forms.DateField(label='Ngày cấp', )
    dia_chi_thuong_tru = forms.CharField(label='Địa chỉ thường trú', max_length=300)
    dia_chi_hien_tai = forms.CharField(label='Địa chỉ hiện tại', max_length=300)
    sdt = forms.CharField(label='Di động/ Phone', max_length=30)
    email = forms.EmailField(label='Email', )
    so_nguoi_phu_thuoc = forms.IntegerField(label='Số người phụ thuộc', )
    # Trình độ học vấn
    TREN_DH = 'TDH'
    DAI_HOC = 'DH'
    CAO_DANG = 'CD'
    TRUNG_CAP = 'TC'
    KHAC = 'KH'
    TRINH_DO_HOC_VAN = (
        (TREN_DH, 'Trên đại học'),
        (DAI_HOC, 'Đại học/University'),
        (CAO_DANG, 'Cao đẳng/ College'),
        (TRUNG_CAP, 'Trung cấp'),
        (KHAC, 'Khác/ Other'))
    trinh_do_hoc_van = forms.ChoiceField(label='Trình độ học vấn/ ', choices=TRINH_DO_HOC_VAN, initial=TREN_DH)

    # Loại nhà ở
    BIET_THU = 'BT'
    NHA_LIEN_KE = 'NLK'
    NHA_DAT = 'ND'
    CHUNG_CU = 'CC'
    LOAI_NHA_O = (
        (BIET_THU, 'Biệt thự/ Villa'),
        (NHA_LIEN_KE, 'Nhà liền kề'),
        (NHA_DAT, 'Nhà đất'),
        (CHUNG_CU, 'Chung cư/ Apartment'),
        (KHAC, 'Khác/ Other'))
    Loai_nha_o = forms.ChoiceField(label='Loại nhà ở/ Type of house', choices=LOAI_NHA_O, initial=BIET_THU)

    # Hình thức sở hữu nhà

    NHA_RIENG = 'NR'
    NHA_DI_THUE = 'NDT'
    NHA_THUE_MUA = 'NTM'
    O_CHUNG_BO_ME = 'OCBM'
    NHA_MUA_TRA_GOP = 'NMTG'
    KHAC = 'KHAC'
    HINH_THUC_O_HUU_NHA = (
        (NHA_RIENG, 'Nhà riêng'),
        (NHA_DI_THUE, 'Nhà đi thuê'),
        (NHA_THUE_MUA, 'Nhà thuê mua'),
        (O_CHUNG_BO_ME, 'Ở chung với bố mẹ(trừ trường hợp bô mẹ cũng đi thuê nhà)'),
        (NHA_MUA_TRA_GOP, 'Nhà mua trả chậm'),
        (KHAC, 'Khác')
    )
    hinh_thuc_so_huu_nha = forms.ChoiceField(label='Hình thức sở hữu nhà/ ', choices=HINH_THUC_O_HUU_NHA, initial=NHA_RIENG)

    # Tình trạng hôn nhân
    DOC_THAN = 'DT'
    DA_CO_GD = 'DCGD'
    LY_DI = 'LD'
    GOA = 'G'
    LY_THAN = 'LT'
    KHAC = 'KH'
    TINH_TRANG_HON_NHAN = (
        (DOC_THAN, 'Độc thân/ Single'),
        (DA_CO_GD, 'Đã có gia đình/ Married'),
        (LY_DI, 'Ly dị'),
        (GOA, 'Goá/ Widow'),
        (LY_THAN, 'Ly thân'),
        (KHAC, 'Khác/Other'))
    tinh_trang_hon_nhan = forms.ChoiceField(label='Tình trạng hôn nhân/ ', choices=TINH_TRANG_HON_NHAN, initial=DOC_THAN)

    class Meta:
        model = ThongTinKhachHang
        fields = '__all__'


