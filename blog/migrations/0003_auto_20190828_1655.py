# Generated by Django 2.2.4 on 2019-08-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190828_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resim',
            field=models.ImageField(upload_to=''),
        ),
    ]
