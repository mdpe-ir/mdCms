# Generated by Django 3.1.7 on 2021-03-02 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pageBuilder', '0002_auto_20210302_1856'),
        ('siteSettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appbarmenu',
            name='pageBuilder',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pageBuilder.pagesmodel'),
        ),
        migrations.AlterField(
            model_name='appbarmenu',
            name='pageUrl',
            field=models.CharField(blank=True, max_length=200, verbose_name='آدرس صفحه'),
        ),
    ]