from django.shortcuts import render,redirect
from AppMy.models import *
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
# Create your views here.

def indexPage(request):
    context = {}
    return render(request, 'index.html', context)

def iletisimPage(request):
    if request.method == "POST":
        ad = request.POST.get("ad")
        soyad = request.POST.get("soyad")
        email = request.POST.get("email")
        telefon = request.POST.get("telefon")
        mesaj = request.POST.get("mesaj")
        iletisim = Iletisim(ad=ad,soyad=soyad,email=email,telefon=telefon,mesaj=mesaj)
        iletisim.save()
        return redirect('/iletisim/')

        


    context = {}

    return render(request, 'iletisim.html', context)
@login_required(login_url="giris")
def iletisimDetayPage(request):
    iletisim_mesajlari = Iletisim.objects.all()
    context = {
        "iletisim": iletisim_mesajlari,
    }
    return render(request, 'iletisim-mesaj.html', context)

def urunlerPage(request,slug = None):
    if slug:
        urunler = Urunler.objects.filter(kategori__slug = slug)
    else:
        urunler = Urunler.objects.all()
    
    context = {
        "urunler": urunler,
    }
    return render(request, 'urunler.html', context)

@login_required(login_url="giris")
def yoneticiPage(request):
    context = {}
    return render(request, 'yonetici.html', context)

from django.shortcuts import get_object_or_404
from .models import kategori, Urunler

@login_required(login_url="giris")
def urun_ekle(request):
    if request.method == "POST":
        ad = request.POST.get("ad")
        fiyat = request.POST.get("fiyat")
        aciklama = request.POST.get("urun_aciklama")
        kategori_adi = request.POST.get("kategoriler")
        urun_resmi = request.FILES.get("urun_resmi")
        
        # Kategori adına göre kategoriyi bul veya oluştur
        kategori_obj, _ = kategori.objects.get_or_create(adi=kategori_adi)
        
        # Urunleri modeline kaydet
        urun = Urunler(adi=ad, fiyat=fiyat, aciklama=aciklama, urun_resmi=urun_resmi, kategori=kategori_obj,slug=slugify(ad))
        urun.save()
        
        return redirect('/urunler/')
    
    context = {}
    return render(request, 'urun_ekle.html', context)

def detailsPage(request,slug):
    if request.method == "POST":
        ad_soyad = request.POST.get("ad_soyad")
        yorum = request.POST.get("yorum")
        yorums= Yorumlar(ad_soyad=ad_soyad,yorum=yorum,urun=Urunler.objects.get(slug = slug))
        yorums.save()
        return redirect(str(request.path))
    
    yorumlar = Yorumlar.objects.filter(urun=Urunler.objects.get(slug = slug))
    urun = Urunler.objects.get(slug = slug)
    context = {
        "urun": urun,
        "yorumlar": yorumlar,
    }
    return render(request, 'details.html', context)

def hakkimizdaPage(request):
    context = {}
    return render(request, 'hakkimizda.html', context)


@login_required(login_url="giris")
def denemePage(request): # Daha sonra silinecek
    urunler = Urunler.objects.all()
    context = {
        "urunler": urunler,
    }
    return render(request, 'deneme.html', context)