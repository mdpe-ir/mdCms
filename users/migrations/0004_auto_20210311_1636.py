# Generated by Django 3.1.7 on 2021-03-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210310_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='2021/03/11', verbose_name='تصویر پروفایل'),
        ),
    ]