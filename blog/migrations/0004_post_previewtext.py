# Generated by Django 3.1.7 on 2021-03-04 17:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210304_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='previewText',
            field=ckeditor.fields.RichTextField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
