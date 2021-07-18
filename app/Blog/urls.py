#Blog.urls

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('base_product',
        views.artical1, name='a1'),

    path('5-hanh-dong-vo-tinh-khien-ban-bi-danh-cap-thong-tin-the',
        views.artical1, name='a1'),
    path('bi-quyet-quan-ly-tai-chinh-chi-tieu-gia-dinh-voi-the-tin-dung',
        views.artical2, name='a2'),
    path('cach-de-nang-cao-diem-tin-dung',
        views.artical3, name='a3'),
    path('tai-sao-the-tin-dung-lai-la-xu-huong-thu-hut',
        views.artical4, name='a4'),


]