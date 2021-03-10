from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from fontawesome_5.fields import IconField


class FooterBlocks(models.Model):
    label = models.CharField(max_length=200)
    content = RichTextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return f" ترتیب :  {self.order} | شناسه : {self.id}"


class FooterSocialMedia(models.Model):
    icon = IconField()
    link = models.URLField()
    order = models.PositiveIntegerField(default=1)

    def get_icons(self):
        return str(self.icon).replace('fab,', '')

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return f"{self.link}"
