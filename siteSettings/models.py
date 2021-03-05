from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from django.db.models import TextField
from django.shortcuts import get_list_or_404

from pageBuilder.models import PagesModel


class BaseSiteSettings(models.Model):
    appBarColor = ColorField(default='#5F788A')
    appBarTextColor = ColorField(default='#FFFFFB')
    appBarTextColorOnHover = ColorField(default='#FFFFFB')
    siteLogo = models.ImageField()

    def __str__(self):
        return f"    فایل تنظیمات {self.id} "


class AppBarMenu(models.Model):
    text = TextField(verbose_name="نام نمایشی")
    pageUrl = models.CharField(max_length=200, verbose_name="آدرس صفحه", blank=True)
    pageBuilder = models.ForeignKey(PagesModel, on_delete=models.SET_NULL, blank=True, null=True, db_constraint=False)

    def get_all_menus(self):
        all_menus = AppBarMenu.objects.all()
        return all_menus

    def __str__(self):
        return self.text
