# Generated by Django 3.1.7 on 2021-03-02 16:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pageBuilder', '0005_pagesmodel_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagesmodel',
            name='html',
            field=ckeditor.fields.RichTextField(),
        ),
    ]