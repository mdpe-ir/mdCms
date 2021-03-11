from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.


class PopupMessages(models.Model):
    ICONS = (

        ('success', 'موفق'),
        ('error', 'ارور'),
        ('warning', 'هشدار'),
        ('info', 'اطلاعات'),
        ('question', 'سوال'),
        ('none', 'بدون آیکون'),

    )

    title = models.CharField(max_length=200)
    messages = RichTextField()
    icon = models.CharField(choices=ICONS, default='info', max_length=100)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.title
