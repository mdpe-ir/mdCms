# Generated by Django 3.1.7 on 2021-03-04 17:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='previewImage',
            field=models.ImageField(default='', upload_to='2021/03/04'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
