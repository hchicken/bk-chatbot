# Generated by Django 2.2.6 on 2021-11-05 17:12

import common.models.base
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("module_intent", "0016_executionlog_rtx"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bot",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(auto_now=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="executionlog",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(auto_now=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="intent",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(auto_now=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="task",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(auto_now=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="utterances",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(auto_now=True, null=True, verbose_name="更新时间"),
        ),
    ]