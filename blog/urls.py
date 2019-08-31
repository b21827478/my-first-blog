from django.urls import path
from . import views

urlpatterns = [
    path('',views.anasayfa),
    path('blog.html',views.blog),
    path('yonetim.html',views.yonetim),
    path('hakkimizda.html', views.hakkimizda),
    path('iletisim.html',views.iletisim),
    path('dersler.html', views.ders_func),

]
