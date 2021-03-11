from django.contrib import admin

# Register your models here.
from popup.models import PopupMessages


class PopupMessagesAdmin(admin.ModelAdmin):
    pass


admin.site.register(PopupMessages, PopupMessagesAdmin)
