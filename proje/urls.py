"""
URL configuration for proje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppMy.views import *
from AppUser.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexPage,name="index"),
    path('kayit/',kayitPage,name="kayit"),
    path('giris/',girisPage,name="giris"),
    path('iletisim/',iletisimPage,name="iletisim"),
    path('urunler/',urunlerPage,name="urunler"),
    path('urunler/<slug>',urunlerPage,name="urunler"),
    path('hakkimizda/',hakkimizdaPage,name="hakkimizda"),
    path("deneme/",denemePage), # Daha sonra silinecek
    path('yonetici/',yoneticiPage,name="yonetici"),
    path('yonetici/urun_ekle',urun_ekle,name="urun_ekle"),
    path('detay/<slug>',detailsPage,name="detay"),
    path('yonetici/hesap_ayarlari',hesap_ayarlariPage,name="hesap_ayarlari"),
    path('/', LogoutView.as_view(), name='logout'),
    path('yonetici/iletisim_mesajlari',iletisimDetayPage,name="iletisim_mesajlari"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
