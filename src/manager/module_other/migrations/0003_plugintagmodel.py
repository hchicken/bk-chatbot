# Generated by Django 2.2.16 on 2022-04-01 15:34

import common.models.base
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_other', '0002_auto_20220318_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='PluginTagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, default='admin', max_length=255, null=True, verbose_name='创建人')),
                ('created_at', common.models.base.FormatDateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('updated_by', models.CharField(blank=True, default='admin', max_length=255, null=True, verbose_name='更新人')),
                ('updated_at', common.models.base.FormatDateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('deleted_by', models.CharField(blank=True, default='admin', max_length=255, null=True, verbose_name='删除人')),
                ('deleted_at', common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name='删除时间')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('key', models.CharField(max_length=64, unique=True, verbose_name='插件标签唯一key')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='插件标签唯一名称')),
            ],
            options={
                'verbose_name': '【插件标签】',
                'verbose_name_plural': '【插件标签】',
                'db_table': 'tab_plugin_tag',
            },
        ),
    ]