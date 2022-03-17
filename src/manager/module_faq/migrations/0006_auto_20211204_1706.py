# Generated by Django 2.2.6 on 2021-12-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_faq', '0005_auto_20211105_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='created_by',
            field=models.CharField(blank=True, default='admin', max_length=255, null=True, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='deleted_by',
            field=models.CharField(blank=True, default='admin', max_length=255, null=True, verbose_name='删除人'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='updated_by',
            field=models.CharField(blank=True, default='admin', max_length=255, null=True, verbose_name='更新人'),
        ),
    ]
