from rest_framework import serializers
from .models import tblDangKyHoc


class DangKyHocserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    khoa_hoc = serializers.CharField(required=True, max_length=264)
    ho_ten = serializers.CharField(required=True, max_length=264)
    dien_thoai = serializers.CharField(required=True, max_length=264)
    email = serializers.EmailField()
    ngay_dang_ky = serializers.DateField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return tblDangKyHoc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.khoa_hoc = validated_data.get('khoa_hoc', instance.khoa_hoc)
        instance.ho_ten = validated_data.get('ho_ten', instance.ho_ten)
        instance.dien_thoai = validated_data.get('dien_thoai', instance.dien_thoai)
        instance.email = validated_data.get('email', instance.email)
        instance.ngay_dang_ky = validated_data.get('ngay_dang_ky', instance.ngay_dang_ky)
        instance.save()
        return instance
    
    class Meta:
        model = tblDangKyHoc
        fields = ('id', 'khoa_hoc', 'ho_ten', 'dien_thoai', 'email', 'ngay_dang_ky')