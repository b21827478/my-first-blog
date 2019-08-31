from django.contrib import admin
from .models import etkinlik,duyurular,dersler

# Register your models here.
admin.site.register(duyurular)
admin.site.register(etkinlik)
admin.site.register(dersler)

