# Generated by Django 2.2.4 on 2019-08-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190830_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='tercihi_mini_baslik',
            field=models.CharField(default='ACM Hacettepe', max_length=50),
        ),
    ]
