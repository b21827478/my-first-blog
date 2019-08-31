# Generated by Django 2.2.4 on 2019-08-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_etkinlik_tercihi_mini_baslik'),
    ]

    operations = [
        migrations.CreateModel(
            name='dersler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duyuru_baslik', models.CharField(default='Ders Adı', max_length=50)),
                ('icerik', models.TextField(default='İçerik ekleyiniz')),
                ('baslangic', models.DateTimeField(blank=True, null=True)),
                ('bitis', models.DateTimeField(blank=True, null=True)),
                ('koordinator', models.CharField(default='Koordinatörlük', max_length=50)),
                ('resim', models.ImageField(upload_to='media')),
            ],
        ),
    ]
