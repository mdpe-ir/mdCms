from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.utils.text import slugify
from django_quill.fields import QuillField
from django_summernote.fields import SummernoteTextFormField
from django_summernote.widgets import *
from tinymce.models import HTMLField


class PagesModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    pageTitle = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    html = RichTextField(extra_plugins=['liststyle'], )

    def __str__(self):
        return self.title
