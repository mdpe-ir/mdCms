from footer.models import FooterBlocks, FooterSocialMedia
from popup.models import PopupMessages
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
        context['copyrightText'] = BaseSiteSettings.objects.all()[0].copyrightText
        context['aboutSite'] = BaseSiteSettings.objects.all()[0].aboutSite

    except Exception as e:
        base_site_settings = BaseSiteSettings()
        base_site_settings.save()

    return context


def get_footer(request):
    context = {}
    footer_block_contents = FooterBlocks.objects.all() or {}
    footer_social_medias = FooterSocialMedia.objects.all() or {}
    context['footer_blocks'] = footer_block_contents
    context['footer_social_medias'] = footer_social_medias
    return context


def show_popup(request):
    context = {}
    popup = PopupMessages.objects.filter(display=True).last() or {}
    context['popup'] = popup
    return context
