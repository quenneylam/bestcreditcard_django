#Blog.views
from django.shortcuts import render

# Create your views here.


def artical1(request):
    return render(request,
                  'Blog/5-hanh-dong-vo-tinh-khien-ban-bi-danh-cap-thong-tin-the.html' )


def artical2(request):
    return render(request,
                  'Blog/bi-quyet-quan-ly-tai-chinh-chi-tieu-gia-dinh-voi-the-tin-dung.html')


def artical3(request):
    return render(request,
                  'Blog/cach-de-nang-cao-diem-tin-dung.html')


def artical4(request):
    return render(request,
                  'Blog/tai-sao-the-tin-dung-lai-la-xu-huong-thu-hut.html')

