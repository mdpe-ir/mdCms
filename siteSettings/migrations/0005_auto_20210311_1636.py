# Generated by Django 3.1.7 on 2021-03-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSettings', '0004_basesitesettings_aboutsite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basesitesettings',
            name='siteLogo',
            field=models.ImageField(upload_to='2021/03/11'),
        ),
    ]
