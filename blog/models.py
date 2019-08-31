from django.db import models
from django.utils import timezone



class etkinlik(models.Model):
    etkinlik_adi=models.CharField(max_length=50,default='Etkinlik Adı')

    tercihi_mini_baslik=models.CharField(max_length=50,default='ACM Hacettepe')


    blog_resim=models.ImageField(upload_to="media")

    slide_resim=models.ImageField(upload_to="media")

    icerik = models.TextField(default="İçerik Ekleyiniz")

    koordinator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    saat_tarih=models.DateTimeField(blank=True,null=True)

    yer=models.CharField(max_length=100,default='Etkinlik Adresi')

    etkinlik_sitesi=models.CharField(max_length=100,default="www.acmhacettepe.com")
class duyurular (models.Model):

    duyuru_baslik=models.CharField(max_length=50,default='Duyuru Adı')

    icerik=models.TextField(default="İçerik ekleyiniz")

    saat_tarih = models.DateTimeField(blank=True, null=True)

    koordinator = models.CharField(max_length=50,default='Koordinatör')

    resim = models.ImageField(upload_to="media")

class dersler (models.Model):

    ders_baslik=models.CharField(max_length=50,default='Ders Adı')

    icerik=models.TextField(default="İçerik ekleyiniz")

    baslangic = models.DateTimeField(blank=True, null=True)
    bitis = models.DateTimeField(blank=True, null=True)

    koordinator = models.CharField(max_length=50,default='Koordinatörlük')

    resim = models.ImageField(upload_to="media")

