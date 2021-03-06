from siteSettings.models import AppBarMenu, BaseSiteSettings
from django.shortcuts import *


def get_menu(request):
    context = {}
    menus = AppBarMenu().get_all_menus()
    context['menus'] = menus

    try:
        context['site_logo'] = BaseSiteSettings.objects.all()[0].siteLogo
        context['appBarColor'] = BaseSiteSettings.objects.all()[0].appBarColor
        context['appBarTextColor'] = BaseSiteSettings.objects.all()[0].appBarTextColor
        context['appBarTextColorOnHover'] = BaseSiteSettings.objects.all()[0].appBarTextColorOnHover
        context['sidebarContent'] = BaseSiteSettings.objects.all()[0].sidebarContent
    except Exception as e:
        baseSiteSettings = BaseSiteSettings()
        baseSiteSettings.save()

    return context
