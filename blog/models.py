from datetime import date

from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

from web.settings import UPLOAD_REGEX


class PostManager(models.Manager):
    def like_toggle(self, user, post_obj):
        if user in post_obj.liked.all():
            is_liked = False
            post_obj.liked.remove(user)
        else:
            is_liked = True
            post_obj.liked.add(user)
        return is_liked


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="عنوان")
    previewImage = models.ImageField(
        upload_to=UPLOAD_REGEX,
        verbose_name="تصویر پیشنمایش")
    content = RichTextField(verbose_name="محتوا")
    previewText = RichTextField(max_length=1000, verbose_name="متن پیش نمایش")
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='liked')
    date_posted = models.DateTimeField(default=timezone.now)

    objects = PostManager()

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.author.username


class SliderContent(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=UPLOAD_REGEX)
    order = models.PositiveIntegerField()
    targetUrl = models.CharField(max_length=200)
    label = RichTextField(blank=True)
    caption = RichTextField(blank=True)

    class Meta:
        ordering = ('order',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_id(self):
        return self.id

    def __str__(self):
        return f" ترتیب :  {self.order} | شناسه : {self.id}"
