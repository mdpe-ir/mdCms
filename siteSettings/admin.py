from django.contrib import admin

# Register your models here.
from siteSettings.models import *

admin.site.register(BaseSiteSettings)
admin.site.register(AppBarMenu)
