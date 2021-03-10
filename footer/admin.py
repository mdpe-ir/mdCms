from django.contrib import admin

# Register your models here.
from footer.models import FooterBlocks, FooterSocialMedia


class FooterBlocksAdmin(admin.ModelAdmin):
    pass


admin.site.register(FooterBlocks, FooterBlocksAdmin)


class FooterSocialMediaAdmin(admin.ModelAdmin):
    pass


admin.site.register(FooterSocialMedia, FooterSocialMediaAdmin)
