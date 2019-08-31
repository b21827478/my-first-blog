from django.shortcuts import render
from .models import etkinlik,duyurular,dersler
from django.utils import timezone


# Create your views here.

def anasayfa(request):
    gonderiler = etkinlik.objects.filter(saat_tarih__lte=timezone.now()).order_by('saat_tarih')
    duyurular_sorted = duyurular.objects.filter(saat_tarih__lte=timezone.now()).order_by('saat_tarih')
    return render(request, 'index.html', {'gonderiler':gonderiler,'duyurular':duyurular_sorted})


def blog(request):
    gonderiler = etkinlik.objects.filter(saat_tarih__lte=timezone.now()).order_by('saat_tarih')
    return render(request, 'blog.html', {'gonderiler':gonderiler})

def yonetim(request):
    gonderiler = etkinlik.objects.filter(saat_tarih__lte=timezone.now()).order_by('saat_tarih')

    return render(request, 'yonetim.html', {'gonderiler': gonderiler})

def hakkimizda(request):
    gonderiler = etkinlik.objects.filter(saat_tarih__lte=timezone.now()).order_by('saat_tarih')

    return render(request, 'hakkimizda.html', {'gonderiler':gonderiler})

def iletisim(request):
    gonderiler = etkinlik.objects.filter(saat_tarih__lte=timezone.now()).order_by('saat_tarih')

    return render(request, 'iletisim.html', {'gonderiler':gonderiler})

def ders_func(request):
    ders = dersler.objects.filter(baslangic__lte=timezone.now()).order_by('baslangic')
    gonderiler = etkinlik.objects.filter(saat_tarih__lte=timezone.now()).order_by('saat_tarih')

    return render(request, 'dersler.html', {'dersler':ders,'gonderiler':gonderiler})

