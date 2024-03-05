from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class kategori(models.Model):
    adi = models.CharField(("Kategori Adı"), max_length=50)
    slug = models.SlugField(("Slug"),null=True)
    def __str__(self):
        return self.adi

class Urunler(models.Model):
    adi = models.CharField(("Ürün Adı"), max_length=50)
    slug = models.SlugField(("Slug"),null=True)
    fiyat = models.IntegerField(("Ürün Fiyatı"),blank=True,null=True)
    urun_resmi = models.ImageField(("Ürün Resmi"), upload_to='urun', max_length=1000)
    aciklama = models.TextField(("Ürün Aciklaması"))
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.adi
    
class Iletisim(models.Model):
    ad = models.CharField(("Ad"), max_length=50)
    soyad = models.CharField(("Soyad"), max_length=50)
    email = models.EmailField(("Email"))
    telefon = PhoneNumberField(("Telefon"))
    mesaj = models.TextField(("Mesaj"))
    def __str__(self):
        return (self.ad+" "+self.soyad)
    

class Yorumlar(models.Model):
    ad_soyad = models.CharField(("Ad Soyad"), max_length=50)
    yorum = models.TextField(("yorum"),null=True)
    tarih = models.DateTimeField(("Tarih"),auto_now_add=True,null=True)
    urun = models.ForeignKey(Urunler, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return (self.ad_soyad)